#!/usr/bin/env python

#pancan = open("../data/Source_Data/PANCAN_mutation_gene","r")
#broad = open("../data/Source_Data/mutation_broad_gene", "r")
#bcgsc = open("../data/Source_Data/mutation_bcgsc_gene", "r")
#
#pancanHeader = pancan.readline().strip().split()
#
#pancanTP53 = []
#for line in pancan:
#	line = line.strip().split()
#	if line[0] == "TP53":
#		pancanTP53 = line
#
#broadHeader = broad.readline().strip().split()
#
#broadTP53 = []
#for line in broad:
#	line = line.strip().split()
#	if line[0] == "TP53":
#		broadTP53 = line
#
#bcgscHeader = bcgsc.readline().strip().split()
#
#bcgscTP53 = []
#for line in bcgsc:
#	line = line.strip().split()
#	if line[0] == "TP53":
#		bcgscTP53 = line
#
#
#outfile = open("temp", "w")
#outfile.write("\t".join(pancanHeader) + "\n")
#outfile.write("\t".join(pancanTP53) + "\n")
#outfile.write("\t".join(broadHeader) + "\n")
#outfile.write("\t".join(broadTP53) + "\n")
#outfile.write("\t".join(bcgscHeader) + "\n")
#outfile.write("\t".join(bcgscTP53) + "\n")

infile = open("temp", "r")
pancanHeader = infile.readline().strip().split()
pancanTP53  = infile.readline().strip().split()
broadHeader = infile.readline().strip().split()
broadTP53 = infile.readline().strip().split()
bcgscHeader = infile.readline().strip().split()
bcgscTP53 = infile.readline().strip().split()

print "Pancan samples: ", len(pancanHeader)
print "Broad samples: ", len(broadHeader)
print "Bcgsc samples: ", len(bcgscHeader)


combined = dict()
for i in range(1, len(pancanHeader)):
	if pancanHeader[i] in combined:
		if combined[pancanHeader[i]] < pancanTP53[i]:
			combined[pancanHeader[i]] = pancanTP53[i]
	else:	
		combined[pancanHeader[i]] = pancanTP53[i]

for i in range(1, len(broadHeader)):
	if broadHeader[i] in combined:
		if combined[broadHeader[i]] < broadTP53[i]:
			combined[broadHeader[i]] = broadTP53[i]
	else:	
		combined[broadHeader[i]] = broadTP53[i]
	
for i in range(1, len(bcgscHeader)):
	if bcgscHeader[i] in combined:
		if combined[bcgscHeader[i]] < bcgscTP53[i]:
			combined[bcgscHeader[i]] = bcgscTP53[i]
	else:	
		combined[bcgscHeader[i]] = bcgscTP53[i]
	

combinedHeader = [x for x in combined]
combinedData = [combined[x] for x in combined]

print "Combined Samples: ", len(combinedHeader)
outfile = open("temp2", "w")
outfile.write("\t".join(combinedHeader)+ "\n")
outfile.write("\t".join(combinedData))

