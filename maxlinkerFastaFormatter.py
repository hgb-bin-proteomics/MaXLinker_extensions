#!/usr/bin/env python3

# Formatter to make Fasta files usable with MaXLinker
# 2022 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

import argparse

__version = "1.0.1"
__date = "20220823"

"""
DESCRIPTION:
A script to re-format fasta files to be usable with MaXLinker.

USAGE:
maxlinkerFastaFormatter.py f [f ...]
                             [-o OUTPUT]
                             [-h]
                             [--version]

positional arguments:
  f                     Fasta file to process, if second filename
                        is given it will be used as the output name!

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Name of the output file.
  --version             show program's version number and exit
"""

# re-formats a given fasta file into MaXLinker compatible format
# input_filename = string (name of the fasta file to format)
# output_filename = string (name of the file that output should be written to)
def format_fasta(input_filename, output_filename):

    with open(input_filename, "r") as f:
        data = f.read()
        f.close()

    entries = data.split(">")

    complete_fasta = ""

    for entry in entries:
        if entry != "":
            lines = entry.split("\n")
            complete_fasta = complete_fasta + ">" + lines[0].rstrip("|") + "|" + lines[0].rstrip("|") + "|" + lines[0].rstrip("|") + "\n" + "".join(lines[1:]) + "\n"

    with open(output_filename, "w") as f:
        f.write(complete_fasta)
        f.close()

# read fasta file and re-format it
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(metavar = "f",
                        dest = "files",
                        help = "Fasta file to process, if second filename is given it will be used as the output name!",
                        type = str,
                        nargs = "+")
    parser.add_argument("-o", "--output",
                        dest = "output",
                        default = None,
                        help = "Name of the output file.",
                        type = str)
    parser.add_argument("--version",
                        action = "version",
                        version = __version)
    args = parser.parse_args()

    input_filename = args.files[0]
    output_filename = args.files[0].split(".fasta")[0] + "_maxlinker.fasta"

    if len(args.files) > 1:
        output_filename = args.files[1].split(".fasta")[0] + ".fasta"

    if args.output is not None:
        output_filename = args.output.split(".fasta")[0] + ".fasta"

    format_fasta(input_filename, output_filename)

if __name__ == "__main__":
    main()
