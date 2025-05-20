# text-file_to_TSV
This script converts a pair of aligned text files into a TSV (Tab-Separated Values) format.

## Overview
The `text-file_to_TSV.py` script takes two plain text files—typically representing source and target language segments—and combines them line-by-line into a `.tsv` file. This format is widely used in data preparation workflows for localization, machine translation, and text-based data processing.

The user provides the paths to the source and target files and specifies the output file name. The resulting `.tsv` file is saved in the same location or path provided.

## Requirements
- Python 3
- The script uses standard Python libraries only (`argparse`, `sys`), which are included with the Python installation.

## Files
`text-file_to_TSV.py`

## Usage
1. Prepare two aligned text files where each line corresponds to a translation unit.
2. Ensure both files use UTF-8 encoding and have the same number of lines.
3. Run the script from the command line as follows:

   ```bash
   python text-file_to_TSV.py source.txt target.txt output.tsv
- source.txt: Path to the source language file (e.g., English).
- target.txt: Path to the target language file (e.g., Spanish).
- output.tsv: Path where the output .tsv file will be saved.
Upon successful execution, a new .tsv file will be created, with each line containing a tab-separated source-target pair.

## Important Note
- The script validates that the number of lines in both input files is identical. If there is a mismatch, an error message is displayed and processing is halted.
- Input files must be encoded in UTF-8. If needed, you can convert your files using any standard text editor or command-line tool.
- The output .tsv file is suitable for use in translation tools, data processing pipelines, or machine learning corpora preparation.

## License
This project is governed by the CC BY-NC 4.0 license. For comprehensive details, kindly refer to the LICENSE file included with this project.
