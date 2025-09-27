import os
import re
import logging
from typing import Optional
from pypdf import PdfReader, PdfWriter


def _get_logger(logger: Optional[logging.Logger], log_level: int) -> logging.Logger:
    """
    Return a logger configured to log to stderr. If a logger is provided, use it.
    """
    if logger is not None:
        return logger

    lg = logging.getLogger("pdf_appendix")
    lg.setLevel(log_level)

    # Avoid adding multiple handlers if function is called repeatedly
    if not lg.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(log_level)
        formatter = logging.Formatter("%(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        lg.addHandler(handler)

    return lg


def add_appendix(
    main_file: str,
    appendix_regex: Optional[str] = None,
    interleave: bool = True,
    *,
    appendix_folder: Optional[str] = None,
    output_folder: Optional[str] = None,
    filename: Optional[str] = None,
    end_pages: int = 0,
    logger: Optional[logging.Logger] = None,
    log_level: int = logging.INFO,
) -> None:
    """
    Merge a main PDF with appendix PDFs files.

    The function:
    - Takes the main PDF file path provided by the user.
    - Looks for appendix files in the same directory (default) or in a
      location provided by the user.
    - Matches the provided regex to find appendix files.
      If no regex is provided, it defaults to '.*_\\d+\\.pdf'
    - Sorts appendices numerically.
    - Optionally interleaves main pages with appendices (default: True).
      If False, appends all appendices together.
    - Preserves the last `end_pages` pages of the main document at the very end.
      Appendices are inserted *before* these preserved tail pages.
    - Produces a new merged file '<main_filename>_with_appendix.pdf'
      (default) or with the filename specified by the user.
    - The merged file is saved to the same directory as the main PDF (default)
      or to a path specified by the user.

    Parameters
    ----------
    main_file : str
        Path to the main PDF file.
    appendix_regex : str, optional
        Regex pattern (without '.pdf') for appendix files.
        Example: 'appendix_\\d+' matches 'appendix_1.pdf'.
        Defaults to '_\\d+' (matches any file ending in _1.pdf, _2.pdf, ...).
    interleave : bool, optional
        If True (default), interleave appendices with the last (N-1) "title" pages
        immediately before the preserved tail. If False, append all appendices
        as a block before the preserved tail.
    appendix_folder : str, optional
        Path to folder containing appendix files.
        Defaults to folder where main_file is located.
    output_folder : str, optional
        Folder where the output file will be saved.
        Defaults to folder where main_file is located.
    filename : str, optional
        Name of output file.
        Defaults to '<main_filename>_with_appendix.pdf'
    end_pages : int, optional
        Number of pages at the end of the main document to keep intact at the end.
        Appendices are placed before these pages. Must be >= 0.
    logger : logging.Logger, optional
        Custom logger. If not provided, a default stdout logger will be used.
    log_level : int, optional
        Logging level for the default logger (e.g. logging.INFO, logging.DEBUG).

    Returns
    -------
    None
        A new merged PDF is written to disk.
    """
    log = _get_logger(logger, log_level)

    if end_pages < 0:
        raise ValueError("end_pages must be >= 0")

    if not os.path.isfile(main_file):
        raise FileNotFoundError(f"Main file not found: {main_file}")

    directory = (
        os.path.dirname(main_file) or "."
    )  # use '.' if file is in current directory
    # Extract filename
    main_filename = os.path.basename(main_file)

    log.info("Main file: %s", main_file)
    log.debug("Main directory resolved to: %s", directory)
    log.debug("Main filename resolved to: %s", main_filename)

    # Build appendix regex pattern
    appendix_pattern = appendix_regex if appendix_regex else r"_\d+"
    appendix_full_pattern = rf".*{appendix_pattern}\.pdf"
    log.info("Looking for appendices matching: %s", appendix_full_pattern)

    appendix_list = []

    # Set appendix folder
    if appendix_folder is None:
        appendix_folder = directory
    else:
        log.info("Appendix folder provided by user: %s", appendix_folder)

    # Find appendix PDFs
    for file in os.listdir(appendix_folder):
        if re.match(appendix_full_pattern, file, flags=re.IGNORECASE):
            match = re.search(r"(\d+)", file)
            number = int(match.group(1)) if match else 0
            appendix_list.append({"number": number, "file": file})
            log.debug("Matched appendix: %s (number=%d)", file, number)

    if not appendix_list:
        raise FileNotFoundError(
            f"No appendix PDFs found in {appendix_folder} (expected pattern '{appendix_full_pattern}')."
        )

    appendix_list.sort(key=lambda x: x["number"])
    n_appendix = len(appendix_list)
    log.info("Found %d appendices:", n_appendix)
    for idx, it in enumerate(appendix_list, 1):
        log.info("  %d) %s (num=%d)", idx, it["file"], it["number"])

    # Open all relevant files safely
    input_files = [open(main_file, "rb")]
    for app in appendix_list:
        input_files.append(open(os.path.join(appendix_folder, app["file"]), "rb"))

    try:
        merger = PdfWriter()
        reader = PdfReader(input_files[0])
        total_pages = len(reader.pages)

        # Raise error if there aren't enough pages in main document to preserve end_pages
        if total_pages < end_pages:
            raise ValueError(
                f"Not enough pages in main to preserve end_pages: total={total_pages}, end_pages={end_pages}"
            )

        if interleave:
            # We will interleave using the (N-1) title pages *before* the preserved tail.
            # Layout:
            # [ head ... | title_page_0 | title_page_1 | ... | title_page_(N-2) | tail(end_pages) ]
            # Appendices go after head, then between title pages, then tail stays last.

            if total_pages < end_pages + max(0, n_appendix - 1):
                # Not enough pages to both preserve tail and interleave with (N-1) title pages
                raise ValueError(
                    "Not enough pages in main document to interleave: "
                    f"total={total_pages}, end_pages={end_pages}, appendices={n_appendix} "
                    "(need at least end_pages + (appendices-1) pages)."
                )

            head_end = total_pages - end_pages - max(0, n_appendix - 1)  # exclusive
            log.info(
                "Interleaving enabled. Head end (exclusive) at %d, preserving last %d pages.",
                head_end,
                end_pages,
            )

            # 1) Head (0 .. head_end-1)
            if head_end > 0:
                merger.append(fileobj=input_files[0], pages=(0, head_end))

            # 2) Interleave appendices with the (N-1) title pages starting at head_end
            for k in range(n_appendix):
                app_name = appendix_list[k]["file"]
                log.info("Appending appendix %d/%d: %s", k + 1, n_appendix, app_name)
                merger.append(fileobj=input_files[1 + k])

                if k < n_appendix - 1:
                    title_idx = head_end + k
                    log.debug("Inserting title page from main at index %d", title_idx)
                    merger.append(fileobj=input_files[0], pages=[title_idx])

            # 3) Tail (the last end_pages pages)
            if end_pages > 0:
                tail_start = total_pages - end_pages
                log.info(
                    "Appending preserved tail: main pages [%d..%d)",
                    tail_start,
                    total_pages,
                )
                merger.append(fileobj=input_files[0], pages=(tail_start, total_pages))

        else:
            # No interleaving: [ head ... | appendices block | tail(end_pages) ]
            head_end = total_pages - end_pages  # exclusive
            log.info(
                "Interleaving disabled. Appending appendices before the last %d preserved pages.",
                end_pages,
            )

            # 1) Head
            merger.append(fileobj=input_files[0], pages=(0, head_end))

            # 2) Appendices block
            for i, app_file in enumerate(input_files[1:], 1):
                log.info(
                    "Appending appendix %d/%d: %s",
                    i,
                    n_appendix,
                    appendix_list[i - 1]["file"],
                )
                merger.append(fileobj=app_file)

            # 3) Tail
            tail_start = total_pages - end_pages
            log.info(
                "Appending preserved tail: main pages [%d..%d)", tail_start, total_pages
            )
            merger.append(fileobj=input_files[0], pages=(tail_start, total_pages))

        # Set output folder according to user input
        if output_folder is None:
            output_folder = directory
        else:
            # Create provided output folder if it does not exist
            os.makedirs(output_folder, exist_ok=True)

        # Set filename according to user input
        if filename is None:
            # Add "_with_appendix.pdf" to the original filename
            root, _ = os.path.splitext(main_filename)
            output_path = os.path.join(output_folder, root + "_with_appendix.pdf")
        else:
            # Use provided filename, add/correct extension if necessary
            root, ext = os.path.splitext(filename)
            if ext != ".pdf":
                filename = root + ".pdf"
                log.debug(f"File extension {ext} overwritten with .pdf")
            output_path = os.path.join(output_folder, filename)
        log.info("Writing output: %s", output_path)
        with open(output_path, "wb") as output:
            merger.write(output)

        log.info("Done.")

    finally:
        # Ensure all files are closed
        for f in input_files:
            try:
                f.close()
            except Exception as e:
                log.debug("Error closing file handle: %s", e)
