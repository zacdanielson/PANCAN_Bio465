#! /usr/bin/env python

import sys
import re

usage = "Usage: ./formatFileName.py gisticPath chrPath outPath"

if len(sys.argv) != 4:
    print usage
    sys.exit(1)

cancerType = sys.argv[1]
chrPath = sys.argv[2]
outPath = sys.argv[3]
chrList = chrPath.split("/")
chr = chrList[len(chrList)- 1]

if chr[:4] == 'TP53':
    #cancerType = "dkajkdf\\dfajkdfj\\fksd\\a_gene_bo_dong"
    cancerList = cancerType.split("/")
    cFileName = cancerList[-1]
    cancer = cFileName.split("_")[0]

    #string  = "TP53.temp"
    pattern = "(TP53).*"
    m = re.match(pattern, chr)
 
else:
    #cancerType = "dkajkdf\\dfajkdfj\\fksd\\a_gene_bo_dong"
    cancerList = cancerType.split("/")
    cFileName = cancerList[-1]
    cancer = cFileName.split("_")[1]

    #string  = "3qGenes.txt"
    pattern = "(\w+)Genes.*"
    m = re.match(pattern, chr)

strConcat = ""

if m:
    strConcat = cancer + "_" + m.group(1)

    outFile = open(outPath + strConcat,"w")
    outFile.close()

print (strConcat)
