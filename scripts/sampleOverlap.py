import os
import subprocess
import sys


inFile = open(sys.argv[1],"r")
outFile = open(sys.argv[2],"w")

cancerDict={}
for sampleList in inFile:
	sampleList = sampleList.strip().split("\t")
	#print sampleList 
	if len(sampleList) > 1:
		cancerType = sampleList[0]
		for i in range(1,len(sampleList)):
			if cancerType in cancerDict:
				cancerDict[cancerType][sampleList[i]] = cancerDict[cancerType][sampleList[i]] + 1 if sampleList[i] in cancerDict[cancerType] else 1
			else:
                    		cancerDict[cancerType] = {sampleList[i]:1} 
				
		#print cancerDict
		#break
	else:	
		continue

deleteAveragesDict = {}

for cancer in cancerDict:
	sDict = cancerDict[cancer]
	sampleCount = len(sDict)
	sum = 0
	for sample in sDict:
		sum += sDict[sample]
	deleteAveragesDict[cancer] = sum/float(sampleCount)

for cancer in cancerDict:
	sampleCount = len(cancerDict[cancer])
	outFile.write(cancer + "\t" + str(sampleCount)+"\t" + "%.1f" % deleteAveragesDict[cancer]+ "\t")
	sampleDict = cancerDict[cancer]
	for s, sample in enumerate(sampleDict):
		if s < sampleCount - 1:
			outFile.write( sample  + " : " +  str(sampleDict[sample]) + "\t")
		else:
			outFile.write( sample  + " : " +  str(sampleDict[sample]))
	outFile.write("\n")
	
outFile.close()
	
'''
    cancerType = inSample.next().strip().split("_")[0]
    for samp in inSamples:
	samp = samp.strip()
	if cancerType in cancerDict:
	else:
		cancerDict[cancerType]= {sampe:1}
	'''
