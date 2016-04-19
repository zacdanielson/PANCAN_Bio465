#! /usr/bin/env python

import sys, os

usage = './sortAnalyseOutput.py analysis.file [-c]\n\t'+\
        'option -c allows for sorting by cancer type\n\t'+\
        'option -3p allows for extracting all lines with 3p chr_arm\n\t'+\
        'default sort option is decreasing order of double to non-double mutations'

if len(sys.argv) not in range(2,4):
    print usage
    print len(sys.argv)
    sys.exit(1)

try:
    with open(sys.argv[1]) as infile:
        analysis_file = [line.strip().split() for line in infile.readlines()]
except IOError:
    print "invalid file\n", usage
    sys.exit(1)

analysis_file2 = []

for line in analysis_file:
    id = line[0].split('/')[-1]
    cancer = id.split('_')[0]
    chr = id.split('_')[1]
    tp53 = line[2]
    tp53_chr = line[1]
    non_combo = str(int(line[3]) - int(line[1]))
    total = line[3]
    line2_item = [id, cancer, chr, tp53, tp53_chr, non_combo, total]
    analysis_file2.append(line2_item)

if len(sys.argv) == 3:
    if sys.argv[2] == "-c":
        analysis_file_sorted = sorted(analysis_file2, key=lambda x: [x[1], float(x[4])/-float(x[6])])
        outfile = os.getcwd() + "/" + sys.argv[1] + "_sorted_type"
    elif sys.argv[2] == "-3p":
        analysis_file3 = [line for line in analysis_file2 if line[2]=='3p']
        analysis_file_sorted = sorted(analysis_file3, key=lambda x: [float(x[4])/-float(x[6])])
        outfile = os.getcwd() + "/" + sys.argv[1] + "_sorted_3p"
    else:
        print "wrong sort option\n", usage
        sys.exit(1)

else:
    analysis_file_sorted = sorted(analysis_file2, key=lambda x: [float(x[4])/float(x[6])], reverse = True)
    outfile = os.getcwd() + "/" + sys.argv[1] + "_sorted"

analysis_file_sorted.insert(0, ["ID", "Cancer_Type", "Chromosome_Arm", "TP53_Mutation_Count", "TP53_ChrArm_event" , "Non-Double_Mutation", "Total"])


print outfile
with open(outfile, 'w') as out:
    out.write('\n'.join(['\t'.join(line) for line in analysis_file_sorted]))
    out.write('\n')

#os.chmod(outfile, 0777)
#os.chown(outfile, -1, 22257)
