#!/usr/bin/env python

from sys import argv
import os
import re

usage = "USAGE: ./genesBySet.py <source_dir> <output_file> <chr_name>\n"
try:
    file = open(argv[1], 'r')

    lines = [line.strip().split() for line in file]

    output = open(argv[2],'w')
    for line in lines:
        if re.match(argv[3], line[0]) is not None:
            output.write(" ".join(line) + '\n')

    file.close()
    output.close()

    if os.path.getsize(argv[2]) == 0:
        print("no lines found")
        os.remove(argv[2])
except Exception:
    print usage
