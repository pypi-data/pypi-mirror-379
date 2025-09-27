import argparse
import logging
from .core import add_appendix
from . import __version__


def main() -> None:
    """
    CLI entry point for pdf-appendix.
    """
    parser = argparse.ArgumentParser(
        description="Merge a main PDF with appendix PDFs from the same directory."
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"pdf-appendix {__version__}",
        help="Show version and exit.",
    )
    parser.add_argument("main_file", help="Path to the main PDF file.")
    parser.add_argument(
        "--pattern",
        "-p",
        dest="appendix_regex",
        help="Regular expression (without '.pdf') to match appendix files. Default: '.*_\\d+'",
        default=None,
    )
    parser.add_argument(
        "--no-interleave",
        dest="interleave",
        action="store_false",
        help="Disable interleaving. Append all appendices at the end instead.",
    )
    parser.add_argument(
        "--end-pages",
        type=int,
        default=0,
        help="Number of pages at the end of the main document to preserve at the end. "
        "Appendices will be inserted before these pages.",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output (DEBUG level logs instead of INFO).",
    )
    parser.add_argument(
        "--appendix-folder",
        "-s",
        dest="appendix_folder",
        help="Folder where appendix files are located.",
    )
    parser.add_argument(
        "--output-folder",
        "-o",
        dest="output_folder",
        help="Folder where output file will be saved.",
    )
    parser.add_argument(
        "--filename",
        "-f",
        dest="filename",
        help="Custom filename for output file.",
    )

    args = parser.parse_args()

    # Decide log level based on --verbose
    log_level = logging.DEBUG if args.verbose else logging.INFO

    add_appendix(
        args.main_file,
        appendix_regex=args.appendix_regex,
        interleave=args.interleave,
        appendix_folder=args.appendix_folder,
        output_folder=args.output_folder,
        filename=args.filename,
        end_pages=args.end_pages,
        log_level=log_level,
    )
