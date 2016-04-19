#!/usr/bin/env python
import sys

path = "../data/"

if len(sys.argv) != 5:
	print "Usage:\n\tinfile.txt outfile.txt genelist.txt samplelist.txt"
	exit(0)

geneFile = open(sys.argv[3], 'r')

geneSets = [line.strip().split() for line in geneFile]
genes = []
for geneSet in geneSets:
	for gene in geneSet:
		genes.append(gene)
print "Number of genes: " + str(len(genes))

sampleFile = open(sys.argv[4],'r')

sampleIds = [line.strip() for line in sampleFile]

print "Number of samples: " + str(len(sampleIds))

inFile = open(sys.argv[1], 'r')
outFile = open(sys.argv[2],'w')

columns = []
newHeader = []
header = inFile.readline().split("\t")
print "Samples in infile: ",len(header)


for i in range(len(header)):
	if header[i] in sampleIds:
		columns.append(i)
		newHeader.append(header[i])
outFile.write("sample\t" + "\t".join(newHeader) + "\n")

print "Samples found: " + str(len(columns)) + " / " + str(len(sampleIds))


genecount = 0

print "# of Columns: ", len(columns)
for line in inFile:
	line = line.split()
	if line[0] in genes:
		genecount += 1
		outFile.write(line[0])
		for i in range(0,len(columns)):
			outFile.write("\t" + line[columns[i]])
		outFile.write("\n")

print "Genes found: " + str(genecount) + " / " + str(len(genes))

inFile.close()
outFile.close()
geneFile.close()
sampleFile.close()
