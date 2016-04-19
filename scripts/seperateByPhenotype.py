#!/usr/bin/env

import sys

if len(sys.argv) != 4:
	print "Usage:\n\tinfile.txt outfile.txt 'phenotype'"
	exit(0)

infile = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")
phenotype = sys.argv[3]

samples = [line.strip().split("\t") for line in infile]

samplesWithPheno = []

count = 0
for sample in samples:
	if sample[21] == phenotype:
		outfile.write(sample[0] + '\n')
		count += 1
print str(count) + " samples found with " + phenotype


	
