# MaXLinker Extensions

Extensions for better usability of the cross-linking tool [MaXLinker](https://www.sciencedirect.com/science/article/pii/S1535947620350416).

## Requirements

MaXLinker requires Python 3.7 (any of the 3.7.xx but not higher or lower than 3.7) and the extension script additionally require pandas and xlsxwriter.
- Install [pandas](https://pandas.pydata.org/): `pip install pandas`
- Install [xlsxwriter](https://xlsxwriter.readthedocs.io/): `pip install xlsxwriter`

## MaXLinker FASTA file converter

```
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
```

Example usage:

```
python maxlinkerFastaFormatter.py human_proteome.fasta -o human_proteome_maxlinker.fasta
```

## MaXLinker crosslink grouper

```
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
                        It's also possible to specify multiple residues e.g.
                        KSTY for DSSO if you want to consider all possible links
  --version             show program's version number and exit
```

Example Usage:

```
python maxlinkerSeqAndPosGrouper.py my_results_uniq.tsv -o results_grouped
```

## MaXLinker to [IMP-X-FDR](https://github.com/fstanek/imp-x-fdr) converter

The main purpose of this script is to convert MaXLinker output files to MS Annika format - which are usable with [IMP-X-FDR](https://github.com/fstanek/imp-x-fdr) tool. This way MaXLinker can be benchmarked on synthetic peptide libraries.

```
DESCRIPTION:
A script to convert MaXLinker *.tsv result files to MS Annika format as
Microsoft Excel worksheets for usage with IMP-X-FDR (v1.1.0).
USAGE:
maxlinkerToAnnikaResultConverter.py f [f ...]
                                      [-o OUTPUT]
                                      [-xl CROSSLINKER]
                                      [-xlmod CROSSLINKER_MODIFICATION]
                                      [-mod MODIFICATIONS]
                                      [-h]
                                      [--version]
positional arguments:
  f                     MaXLinker result file to process, if second filename
                        is given it will be used as the output name!
optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Name of the output file.
  -xl CROSSLINKER, --crosslinker CROSSLINKER
                        Name of the Crosslinker e.g. DSSO.
  -xlmod CROSSLINKER_MODIFICATION, --crosslinker-modification CROSSLINKER_MODIFICATION
                        Residue that the Crosslinker binds to e.g. K for DSSO.
                        It's also possible to specify multiple residues e.g.
                        KSTY for DSSO if you want to consider all possible links
  -mod MODIFICATIONS, --modifications MODIFICATIONS
                        Modifications as dictionary string / in json format.
  --version             show program's version number and exit
```

Example Usage:

```
python maxlinkerToAnnikaResultConverter.py my_results_uniq.tsv -o my_results_converted -xl DSSO -xlmod KSTY -mod "{\"M\": \"Oxidation\", \"C\": \"Carbamidomethyl\"}"
```

## License

[MIT License](https://github.com/hgb-bin-proteomics/MaXLinker_extensions/blob/master/LICENSE)

## Contact

[micha.birklbauer@fh-hagenberg.at](mailto:micha.birklbauer@fh-hagenberg.at)
