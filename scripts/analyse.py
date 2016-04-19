#!/usr/bin/env python

import sys

if len(sys.argv) != 3:
	print "Usage: analyzeData.py tp53file.txt chrFile.txt"
	exit(0)

tp53file = open(sys.argv[1], "r")
chrFile = open(sys.argv[2], "r")

tp53Header = tp53file.readline().strip().split()
tp53Data = tp53file.readline().strip().split()

chrHeader = chrFile.readline().strip().split()
chrData = [line.strip().split() for line in chrFile]


tp53 = set()
for i in tp53Header:
	tp53.add(i)
totalcount = 0
for i in chrHeader:
	if i in tp53:
		totalcount +=1

withMutation = set()
for i in range(1,len(tp53Header)):
	if tp53Data[i] == '1.0' or tp53Data[i] == "1":
		withMutation.add(tp53Header[i])

argList = sys.argv[2].split("/")
cancerType = argList[len(argList)-1].split("_")[0]
sampleList = [cancerType]
outSample = open("cancerPatients.txt","a")


deletions= dict()
for i in range(len(chrHeader)):
	if chrHeader[i] in withMutation:
		for j in range(len(chrData)):
			if chrData[j][i] == "-1" or chrData[j][i] == "-2":
				if chrHeader[i] in deletions:
					deletions[chrHeader[i]].append(chrData[j][0])
				else:
					deletions[chrHeader[i]] = [chrData[j][0]]
argList = sys.argv[2].split("/")
cancerType = argList[len(argList)-1].split("_")[0]
sampleList = [cancerType]
count = 0
for sample in deletions:
	if len(deletions[sample]) > 639:
		count += 1
		sampleList.append(sample)
outSample.write("\t".join(sampleList) + "\n")
outSample.close()
print sys.argv[2], count, len(withMutation), totalcount
