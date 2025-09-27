# tests/test_core.py

from pathlib import Path
import pytest
from pypdf import PdfReader, PdfWriter
from pdf_appendix.core import add_appendix

# Reuse your generator function
from tests.generate_test_pdfs import create_pdf


def _page_has(reader: PdfReader, index: int, needle: str) -> bool:
    txt = reader.pages[index].extract_text() or ""
    return needle in txt


@pytest.fixture
def generated_pdfs(tmp_path: Path):
    """
    Generate in a temp dir:
      - main.pdf (20 pages) titled "main - Page i"
      - appendix_1.pdf .. appendix_5.pdf titled "appendix N - Page i" with 1..5 pages
    """
    # Main document (20 pages, title "main")
    main = tmp_path / "main.pdf"
    create_pdf(main, 20, "main")

    # Appendices: 1..5 pages
    for n in range(1, 6):
        create_pdf(tmp_path / f"appendix_{n}.pdf", n, f"appendix {n}")

    return tmp_path, main


def test_merge_no_interleave(generated_pdfs):
    _, main = generated_pdfs

    # Append all appendices as a block at the end
    add_appendix(str(main), interleave=False, log_level=0)

    out = main.with_name("main_with_appendix.pdf")
    assert out.exists(), "Output PDF was not created"

    r = PdfReader(str(out))

    # Expected pages: 20 (main) + (1+2+3+4+5)=15 (appendices) = 35
    assert len(r.pages) == 35

    # Sanity: first page is from main
    assert _page_has(r, 0, "main - Page 1")

    # The first appended page immediately after main's 20 pages is "appendix 1 - Page 1"
    assert _page_has(r, 20, "appendix 1 - Page 1")

    # The very last page should be the end of appendix 5
    assert _page_has(r, 34, "appendix 5 - Page 5")


def test_merge_with_interleave(generated_pdfs):
    _, main = generated_pdfs

    # Interleaving enabled (default)
    add_appendix(str(main), interleave=True, log_level=0)

    out = main.with_name("main_with_appendix.pdf")
    assert out.exists(), "Output PDF was not created"

    r = PdfReader(str(out))

    # Same total length as non-interleaved: 35
    assert len(r.pages) == 35

    # With 5 appendices, the algorithm interleaves after the first (20 - (5-1)) = 16 pages
    head_end = 16  # 0-based index where interleave region starts

    # Head: first 16 pages should be main
    assert _page_has(r, 0, "main - Page 1")
    assert _page_has(r, 15, "main - Page 16")

    idx = head_end

    # Then we expect: App1, main p17, App2 (2 pages), main p18, App3 (3 pages), main p19, App4 (4 pages), main p20, App5 (5 pages)

    # App1 (1 page)
    assert _page_has(r, idx, "appendix 1 - Page 1")
    idx += 1

    # Main page 17
    assert _page_has(r, idx, "main - Page 17")
    idx += 1

    # App2 (2 pages)
    assert _page_has(r, idx, "appendix 2 - Page 1")
    assert _page_has(r, idx + 1, "appendix 2 - Page 2")
    idx += 2

    # Main page 18
    assert _page_has(r, idx, "main - Page 18")
    idx += 1

    # App3 (3 pages)
    for p in range(1, 4):
        assert _page_has(r, idx, f"appendix 3 - Page {p}")
        idx += 1

    # Main page 19
    assert _page_has(r, idx, "main - Page 19")
    idx += 1

    # App4 (4 pages)
    for p in range(1, 5):
        assert _page_has(r, idx, f"appendix 4 - Page {p}")
        idx += 1

    # Main page 20
    assert _page_has(r, idx, "main - Page 20")
    idx += 1

    # App5 (5 pages)
    for p in range(1, 6):
        assert _page_has(r, idx, f"appendix 5 - Page {p}")
        idx += 1

    # We should be exactly at the end
    assert idx == len(r.pages)


def test_merge_no_interleave_with_end_pages(generated_pdfs):
    _, main = generated_pdfs

    # Append all appendices as a block at the end leaving to pages of the original document
    add_appendix(str(main), interleave=False, end_pages=2, log_level=0)

    out = main.with_name("main_with_appendix.pdf")
    assert out.exists(), "Output PDF was not created"

    r = PdfReader(str(out))

    # Expected pages: 20 (main) + (1+2+3+4+5)=15 (appendices) = 35
    assert len(r.pages) == 35

    # Sanity: first page is from main
    assert _page_has(r, 0, "main - Page 1")

    # The first appended page after main's 18th page is "appendix 1 - Page 1"
    assert _page_has(r, 18, "appendix 1 - Page 1")

    # The last page of the apendix section is "appendix 5 - Page 5"
    assert _page_has(r, 32, "appendix 5 - Page 5")

    # The last two pages are from the original document
    assert _page_has(r, 33, "main - Page 19")
    assert _page_has(r, 34, "main - Page 20")


def test_merge_with_interleave_with_end_pages(generated_pdfs):
    _, main = generated_pdfs

    # Interleaving enabled (default) with 2 end pages
    add_appendix(str(main), interleave=True, end_pages=2, log_level=0)

    out = main.with_name("main_with_appendix.pdf")
    assert out.exists(), "Output PDF was not created"

    r = PdfReader(str(out))

    # Same total length as non-interleaved: 35
    assert len(r.pages) == 35

    # With 5 appendices and 2 end pages, the algorithm interleaves after the first (20 - 2 - (5-1)) = 14 pages
    head_end = 14  # 0-based index where interleave region starts

    # Head: first 14 pages should be main
    assert _page_has(r, 0, "main - Page 1")
    assert _page_has(r, 13, "main - Page 14")

    idx = head_end

    # Then we expect: App1, main p15, App2 (2 pages), main p16, App3 (3 pages), main p17, App4 (4 pages), main p18, App5 (5 pages), main p19 and p20.

    # App1 (1 page)
    assert _page_has(r, idx, "appendix 1 - Page 1")
    idx += 1

    # Main page 15
    assert _page_has(r, idx, "main - Page 15")
    idx += 1

    # App2 (2 pages)
    assert _page_has(r, idx, "appendix 2 - Page 1")
    assert _page_has(r, idx + 1, "appendix 2 - Page 2")
    idx += 2

    # Main page 16
    assert _page_has(r, idx, "main - Page 16")
    idx += 1

    # App3 (3 pages)
    for p in range(1, 4):
        assert _page_has(r, idx, f"appendix 3 - Page {p}")
        idx += 1

    # Main page 17
    assert _page_has(r, idx, "main - Page 17")
    idx += 1

    # App4 (4 pages)
    for p in range(1, 5):
        assert _page_has(r, idx, f"appendix 4 - Page {p}")
        idx += 1

    # Main page 18
    assert _page_has(r, idx, "main - Page 18")
    idx += 1

    # App5 (5 pages)
    for p in range(1, 6):
        assert _page_has(r, idx, f"appendix 5 - Page {p}")
        idx += 1

    # Main page 19
    assert _page_has(r, idx, "main - Page 19")
    idx += 1

    # Main page 20
    assert _page_has(r, idx, "main - Page 20")
    idx += 1

    # We should be exactly at the end
    assert idx == len(r.pages)


def test_appendix_folder_different(tmp_path: Path):
    """
    Appendices live in a different folder than the main document.
    Expect the tool to find them via `appendix_folder` and write the
    output next to the main file (default naming).
    """
    # Arrange
    main = tmp_path / "main.pdf"
    appendices_dir = tmp_path / "appendices"
    appendices_dir.mkdir()

    # Main document (20 pages)
    create_pdf(main, 20, "main")

    # Appendices (1..5 pages) created in a DIFFERENT directory
    for n in range(1, 6):
        create_pdf(appendices_dir / f"appendix_{n}.pdf", n, f"appendix {n}")

    # Act
    add_appendix(
        str(main),
        interleave=False,
        appendix_folder=str(appendices_dir),
        log_level=0,
    )

    # Assert
    out = main.with_name("main_with_appendix.pdf")
    assert out.exists(), "Output PDF was not created in main's folder"

    r = PdfReader(str(out))
    # 20 main + 15 appendices
    assert len(r.pages) == 35
    # Sanity: first main page and last page of last appendix present
    assert _page_has(r, 0, "main - Page 1")
    assert _page_has(r, 34, "appendix 5 - Page 5")


def test_custom_filename(generated_pdfs):
    """
    Provide a custom output filename.
    Expect the file to be created with that exact name in the main dir.
    """
    tmp_path, main = generated_pdfs
    custom_name = "my_custom_output.pdf"

    add_appendix(
        str(main),
        interleave=False,
        filename=custom_name,
        log_level=0,
    )

    out = tmp_path / custom_name
    assert out.exists(), "Custom-named output PDF was not created"

    r = PdfReader(str(out))
    assert len(r.pages) == 35
    # Quick sanity checks
    assert _page_has(r, 0, "main - Page 1")
    assert _page_has(r, 20, "appendix 1 - Page 1")


def test_custom_output_folder(generated_pdfs):
    """
    Provide a custom output folder.
    Expect the output to be written there with the default naming.
    """
    tmp_path, main = generated_pdfs
    out_dir = tmp_path / "out"
    out_dir.mkdir()

    add_appendix(
        str(main),
        interleave=False,
        output_folder=str(out_dir),
        log_level=0,
    )

    # Default naming: <main_stem>_with_appendix.pdf
    out = out_dir / "main_with_appendix.pdf"
    assert out.exists(), "Output PDF was not created in the specified output folder"

    r = PdfReader(str(out))
    assert len(r.pages) == 35
    # Spot-check beginning and end
    assert _page_has(r, 0, "main - Page 1")
    assert _page_has(r, 34, "appendix 5 - Page 5")
