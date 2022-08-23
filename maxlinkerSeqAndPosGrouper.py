#!/usr/bin/env python3

# MaXLinker crosslink grouper (by sequence and position)
# 2022 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

import argparse
import pandas as pd

__version = "1.0.0"
__date = "20220823"

"""
DESCRIPTION:
A script to group crosslinks from MaXLinker results files by sequence and position.

USAGE:
maxlinkerSeqAndPosGrouper.py f [f ...]
                               [-o OUTPUT]
                               [-xlmod CROSSLINKER_MODIFICATION]
                               [-h]
                               [--version]

positional arguments:
  f                     MaXLinker result file to process, if second filename
                        is given it will be used as the output name!

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Name of the output file.
  -xlmod CROSSLINKER_MODIFICATION, --crosslinker-modification CROSSLINKER_MODIFICATION
                        Residue that the Crosslinker binds to e.g. K for DSSO.
  --version             show program's version number and exit
"""

# get the position of the crosslinker in an amino acid sequence
# sequence = string (the amino acid sequence)
# xl_modification = string (the one-letter-code of the amino acid that reacts with the crosslinker)
def get_crosslinker_position(sequence, xl_modification = "k"):

    i = 0
    for AA in sequence:
        if AA.isupper():
            i += 1
        else:
            if AA == xl_modification.lower():
                return i
            else:
                i += 1

    return i

# group crosslinks by sequence and position
# input_filename = string (the name of the MaXLinker result file)
# xl_modification = string (the one-letter-code of the amino acid that reacts with the crosslinker)
def group_by_sequence_and_position(input_filename, xl_modification = "k"):

    df = pd.read_csv(input_filename, sep = "\t")

    unique_xl = dict()

    for index, row in df.iterrows():
        pep_a = row["Peptide A"]
        pep_b = row["Peptide_B"]
        sequences_and_positions = [pep_a.upper() + str(get_crosslinker_position(pep_a, xl_modification)),
                                   pep_b.upper() + str(get_crosslinker_position(pep_b, xl_modification))]
        sequences_and_positions.sort()
        key = "-".join(sequences_and_positions)
        if key in unique_xl:
            if unique_xl[key]["Score"] < row["Score"]:
                unique_xl[key] = row
        else:
            unique_xl[key] = row

    df_grouped = pd.DataFrame.from_dict(unique_xl, orient = "index")

    return df_grouped

# group crosslinks and create new result file
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(metavar = "f",
                        dest = "files",
                        help = "MaXLinker result file to process, if second filename is given it will be used as the output name!",
                        type = str,
                        nargs = "+")
    parser.add_argument("-o", "--output",
                        dest = "output",
                        default = None,
                        help = "Name of the output file.",
                        type = str)
    parser.add_argument("-xlmod", "--crosslinker-modification",
                        dest = "crosslinker_modification",
                        default = "K",
                        help = "Residue that the Crosslinker binds to e.g. K for DSSO.",
                        type = str)
    parser.add_argument("--version",
                        action = "version",
                        version = __version)
    args = parser.parse_args()

    input_filename = args.files[0]
    output_filename = args.files[0].split(".tsv")[0] + "_gbSeqPos.tsv"

    if len(args.files) > 1:
        output_filename = args.files[1].split(".tsv")[0] + ".tsv"

    if args.output is not None:
        output_filename = args.output.split(".tsv")[0] + ".tsv"

    df_grouped = group_by_sequence_and_position(input_filename, args.crosslinker_modification)

    df_grouped.to_csv(output_filename, sep = "\t", index = False)

if __name__ == "__main__":
    main()
