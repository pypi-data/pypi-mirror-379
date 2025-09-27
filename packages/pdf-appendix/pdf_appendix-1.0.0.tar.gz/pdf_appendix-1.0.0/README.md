# 📑 pdf-appendix

[![PyPI version](https://img.shields.io/pypi/v/pdf-appendix.svg)](https://pypi.org/project/pdf-appendix/)


pdf-appendix is a lightweight command-line tool for merging appendix PDFs into a main document.

It is designed for reports where the main document contains title pages for each appendix, and the appendices need to be inserted at the right spots.

---

## ✨ Features

- 📂 Merge multiple appendices into a main PDF
- 🔀 Interleave appendices with main document title pages, or append as a block
- 📑 Preserve the last N pages of the main document at the end (```--end-pages```)
- 📁 Use appendices from a custom folder (```--appendix-folder```)
- 📂 Save the merged PDF in a custom folder (```--output-folder```)
- 📝 Set a custom output filename (```--filename```)
- 🔍 Regex-based appendix file matching (```--pattern```)
- 📊 Verbose logging for debugging (```--verbose```)
---

## ⚙️ Installation
Install from [PyPI](https://pypi.org/project/pdf-appendix/) with pip:

```bash
pip install pdf-appendix
```

## 📖 Usage

Run from the command line:

```bash
pdf-appendix main.pdf
```

## 🔍 Options

- ```--pattern```: Regex for appendix filenames (default: "_\d+")

- ```--no-interleave```: Append all appendices as one block instead of interleaving

- ```--end-pages``` N: Preserve the last N pages of the main document at the very end

- ```--appendix-folder PATH```: Folder where appendix PDFs are stored (default: same as main file)

- ```--output-folder PATH```: Folder where the merged PDF will be saved (default: same as main file)

- ```--filename NAME```: Custom output filename (default: ```<main>_with_appendix.pdf```)

- ```--verbose```: Show detailed debug output

## Examples
```bash
# Append appendix files like report_1.pdf, report_2.pdf ...
pdf-appendix report.pdf

# Match files appendix_1.pdf, appendix_2.pdf ...
pdf-appendix report.pdf --pattern "appendix_\d+"

# Append all appendices at the end (no interleaving)
pdf-appendix report.pdf --no-interleave

# Preserve last 2 pages of main document
pdf-appendix report.pdf --end-pages 2

# Use appendices from a different folder
pdf-appendix report.pdf --appendix-folder ./appendices

# Save output in a different folder
pdf-appendix report.pdf --output-folder ./output

# Save output with a custom filename
pdf-appendix report.pdf --filename merged.pdf

# Verbose output (DEBUG level)
pdf-appendix report.pdf --verbose
```

## 📑 About Interleaving

The ```--interleave``` option is intended for cases where your main document already includes placeholder title pages for each appendix (e.g. a page that says “Appendix 1”, “Appendix 2”, …).

When ```--interleave``` is enabled (default):

The tool inserts each appendix directly after its corresponding title page in the main document.

When ```--no-interleave```:

All appendices are simply appended at the end of the main document in order.

This allows you to prepare a clean report with dedicated appendix cover pages and let the tool place the actual appendix content in the right spots automatically.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/HasbunWoodEngineering/pdf-appendix/blob/main/LICENSE) file for details.

## Third-Party Licenses

This project makes use of the following third-party library:

- [pypdf](https://github.com/py-pdf/pypdf) — licensed under the BSD-3-Clause License

Build tools and development dependencies (such as  `black` and `pytest`) are licensed under permissive licenses (MIT or similar) and are only used during development and packaging.

See [THIRD_PARTY_LICENSES](https://github.com/HasbunWoodEngineering/pdf-appendix/blob/main/THIRD_PARTY_LICENSES) for details.