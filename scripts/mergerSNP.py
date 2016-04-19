import sys
import os


'''
arg 0 file script
> arg 0 is input snp tables to be merged
I hard coded the output file, sorry and file path into data folder
'''

listOfTables =[]
for i in range(1,lenOfArg):
    listOfTables.append(open(sys.argv[i],'r'))


def writeTP53(gene):


    filename = "TP53Merged.txt"
    path = "../data"
    fullpath = os.path.join(path, filename)
    print fullpath
    outFile = open(fullpath,'w')

    patientDict = snpDict[gene]
    patientName = []
    values = []
    tp53Dict = snpDict["TP53"]
    for key in tp53Dict:
        patientName.append(key)
        values.append(tp53Dict[key])
    header = "sample\t" + "\t".join(patientName)
    values = "data\t" + "\t".join(values)
    wholeTable = header + "\n" + values
    outFile.write(wholeTable)
    outFile.close()


def mergeSNPTable(table):
    firstLine = table.next().strip().split("\t")
    #print firstLine

    for row in table:
        row = row.strip().split("\t")
        colLength = len(row) - 1
        if row[0] == "TP53":

            if row[0] not in snpDict:
                snpDict[row[0]] = {} # new gene and intialize first patient(column)

            for i in xrange(1,colLength):
                if firstLine[i] in snpDict[row[0]]:   # patients associated with that gene
                    value = snpDict[row[0]][firstLine[i]]
                    if (value < row[i]): # Same pateint same different value side with mutation or 1
                        snpDict[row[0]][firstLine[i]]= row[i]

                else:
                    snpDict[row[0]].update({firstLine[i]:row[i]})


            #value=  snpDict[row[0]].get(firstLine[i])






snpDict= {}

for table in listOfTables:
    mergeSNPTable(table)

writeTP53("TP53")

for table in listOfTables:
    table.close()

count = 0
#for file in Directory:

#patientHeader = table.next().strip().split("\t")





