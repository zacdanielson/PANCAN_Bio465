#!/bin/bash

if (($# != 3)); then
	echo Usage: automateReduce.sh sample_path mergedTP53_file out_file
	exit $? 
fi

samplePath=$1
mergedTP53=$2
outPath=$3
scriptsPath=$(pwd)
tp53Path="/fslhome/be3sleyc/fsl_groups/fslg_pancan465/PANCAN/data/TP53.dir/TP53.temp"

ls -1 $samplePath | tr "\\n" "\\n" > $scriptsPath"/sampleFileNames.txt"

#cat sampleFileNames.txt

mapfile -t sArray < sampleFileNames.txt

rm "sampleFileNames.txt"

scount=${#sArray[@]}  # gets number of sample files
	
for i in `seq 0 $(($scount - 1))`
    do
        outFile=`python ./formatFileName.py $samplePath${sArray[i]} $tp53Path $outPath`
        echo $outFile
        python ./reduceFile.py $mergedTP53 $outPath$outFile $tp53Path $samplePath${sArray[i]}
        chmod 777 $outPath$outFile
        chown :fslg_pancan465 $outPath$outFile
    done

