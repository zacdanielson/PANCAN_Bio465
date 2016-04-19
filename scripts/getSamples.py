#! /usr/bin/env python 

import os 
import sys

usage = "Used to extract sample ids from files or directories of files. Output is written to /PANCAN/data/samples\n"+\
        "Usage:\n"+\
        "\t./getSamples.py <-f|-d> <target>\n"+\
        "\t\t<-f|-d>: file or directory\n"+\
        "\t\t<target> file or directory path with sample ids\n"

def fileSamples(input_file, output_file):
    print("scanning " + input_file)
    input = open(input_file, "r")
    samples = "\n".join(input.readline().strip().split()[1:])
    input.close()
    print("found {0} sample ids in {1}".format(samples.count("\n"), input_file))
    output_file.write(samples)

if len(sys.argv) == 3:
    if sys.argv[1] == '-f':
        print("files")
        if os.path.isfile(sys.argv[2]):
            outfile = sys.argv[2].split("_")[1] + "_sample_ids.txt" 
            output = open("/fslhome/be3sleyc/fsl_groups/fslg_pancan465/PANCAN/data/samples/"+ outfile, "w")
            fileSamples(sys.argv[2], output)
            output.close()
            print("done")
        else:
            print("target is not a file")
            print usage

    elif sys.argv[1] == '-d':
        cwd = sys.argv[2]
        for file in os.listdir(cwd):
            if os.path.isfile(file):
                outfile = file.split("_")[1] + "_sample_ids.txt"
                output = open("/fslhome/be3sleyc/fsl_groups/fslg_pancan465/PANCAN/data/samples/"+ outfile, "w")
                fileSamples(file, output)
                output.close()
        print("done")
    else:
        print("incorrect option\n")
        print usage
else:
    print usage
