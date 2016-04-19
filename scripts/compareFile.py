#!/usr/bin/env python

import sys

if len(sys.argv) != 3:
	print "Usage: compareFile.py file1 file"
	exit(0)

file1 = open(sys.argv[1], 'r')
file2= open(sys.argv[2],'r')

header1 = file1.readline().strip().split("\t")
header2 = file2.readline().strip().split("\t")

if len(header1) != len(header2):
	print "DIFFERENCE IN LENGTH"
	print "File 1 has",len(header1),"samples"
	print "File 2 has",len(header2),"samples"

for sample in header1:
	if sample not in header2:
		print "DIFFERENCE!!!!!"
		print "Sample",sample,"not in file 2"

for sample in header2:
	if sample not in header1:
		print "DIFFERENCE!!!!!"
		print "Sample",sample,"not in file 1"
