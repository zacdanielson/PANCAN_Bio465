#!/usr/bin/env python

from sys import argv

usage = "USAGE: ./generateGeneList.py <source_file_path> <output_file>\n"
try:
    file = open(argv[1],'r')

    geneSets = [line.strip().split() for line in file]

    genes = []

    for geneSet in geneSets:
	for i in range(2,len(geneSet)):
	    genes.append(geneSet[i])

    outfile = open(argv[2],'w')
    outfile.write("\n".join(genes))
except Exception:
    print usage

