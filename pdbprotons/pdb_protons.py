#!/usr/local/bin/python

import numpy as np
import os as os

"""
Program reads a text file in PDB format and outputs two tables: 
Table 1 - Atom numbers with bond lengths and bond angle.
Table 2 - Residue number with phi, psi, and omega dihedral angles. 
"""

INPUT_FILENAME = "TBRII-CLBT-LukaszModel-withH.pdb"


def main():
    output_filename = make_output_file()

    input_file = open(INPUT_FILENAME, 'r')
    output_file = open(output_filename, 'w')
    for line in input_file:
        if line[0:4] == "ATOM" and line[13] is "H":  # Filter based on PDB file structure and atom type
            line = line[:13] + "H  " + line[16:]
            output_file.write(line)
        else:
            output_file.write(line)
    output_file.close()
    input_file.close()


def make_output_file():
    directory = os.getcwd()
    name = INPUT_FILENAME.split()[0]
    return os.path.join(directory, name[:-4] + "_output.pdb")


main()
