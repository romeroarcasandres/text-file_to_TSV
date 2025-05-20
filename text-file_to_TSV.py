#!/usr/bin/env python3
import argparse
import sys

def convert_to_tsv(source_file, target_file, output_file):
    """
    Convert two text files into a single TSV file.
    
    Args:
    source_file (str): Path to the first source text file (UTF-8 encoded)
    target_file (str): Path to the second target text file (UTF-8 encoded)
    output_file (str): Path to the output TSV file
    """
    try:
        # Read source file with UTF-8 encoding
        with open(source_file, 'r', encoding='utf-8') as src:
            source_lines = src.readlines()
        
        # Read target file with UTF-8 encoding
        with open(target_file, 'r', encoding='utf-8') as tgt:
            target_lines = tgt.readlines()
        
        # Ensure both files have the same number of lines
        if len(source_lines) != len(target_lines):
            print(f"Error: Source file ({len(source_lines)} lines) and target file ({len(target_lines)} lines) have different line counts.")
            sys.exit(1)
        
        # Write to TSV file with UTF-8 encoding
        with open(output_file, 'w', encoding='utf-8') as tsv_out:
            for src_line, tgt_line in zip(source_lines, target_lines):
                # Strip whitespace and newline characters
                src_line = src_line.strip()
                tgt_line = tgt_line.strip()
                
                # Write tab-separated line
                tsv_out.write(f"{src_line}\t{tgt_line}\n")
        
        print(f"Successfully converted files to TSV: {output_file}")
    
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        sys.exit(1)
    except PermissionError:
        print("Error: Permission denied when trying to read or write files.")
        sys.exit(1)
    except UnicodeDecodeError:
        print("Error: Files must be encoded in UTF-8. Please check file encodings.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Convert two UTF-8 text files to a TSV file.')
    parser.add_argument('source_file', help='Path to the first source text file')
    parser.add_argument('target_file', help='Path to the second target text file')
    parser.add_argument('output_file', help='Path to the output TSV file')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call conversion function
    convert_to_tsv(args.source_file, args.target_file, args.output_file)

if __name__ == '__main__':
    main()