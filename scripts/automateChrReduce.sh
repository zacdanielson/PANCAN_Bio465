#!/bin/bash

if (($# != 4)); then
	echo Usage: automateReduce.sh gistic_path sample_path chr_gene_path out_file 
	exit $? 
fi

gisticPath=$1
samplePath=$2
chrPath=$3
outPath=$4
scriptsPath=$(pwd)

ls -1 $gisticPath | tr "\\n" "\\n" > $scriptsPath"/gisticFileNames.txt"
ls -1 $samplePath | tr "\\n" "\\n" > $scriptsPath"/sampleFileNames.txt"
ls -1 $chrPath | tr "\\n" "\\n" > $scriptsPath"/chrFileNames.txt"

#cat gisticFileNames.txt
#cat sampleFileNames.txt
#cat chrFileNames.txt

mapfile -t gArray < gisticFileNames.txt
mapfile -t sArray < sampleFileNames.txt
mapfile -t cArray < chrFileNames.txt

rm "gisticFileNames.txt"
rm "sampleFileNames.txt"
rm "chrFileNames.txt"

gcount=${#gArray[@]} # gets number of gistic files
scount=${#sArray[@]}  # gets number of sample files
ccount=${#cArray[@]}
if (($gcount == $scount)); then
	
	for i in `seq 0 $(($gcount - 1))`
		do
                    for chr in `seq 0 $(($ccount - 1))`
                        do
                            outFile=`./formatFileName.py $gisticPath${gArray[i]}  ${cArray[chr]} $outPath`
                            echo $outFile
			    ./reduceFile.py $gisticPath${gArray[i]} $outPath$outFile $chrPath${cArray[chr]} $samplePath${sArray[i]}
                            chmod 777 $outPath$outFile
                            chown :fslg_pancan465 $outPath$outFile
			done
		done
fi
