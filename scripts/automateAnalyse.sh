#!/bin/bash

if (($# != 3)); then
	echo Usage: automateAnalyse.sh reduced_cancer_path/ reduced_tp53_path/ out_file
	exit $? 
fi

redCancerPath=$1
redTP53Path=$2
outFile=$3
currentPath=$(pwd)
scriptsPath="/panfs/pan.fsl.byu.edu/home/grp/fslg_pancan465/PANCAN/scripts/"
analyse="analyse.py"
pysort="sortAnalyseOutput.py"

regex="(\w+)_.*"

ls -1 $redCancerPath | tr "\\n" "\\n" > $currentPath"/reduced_cancers.txt"
ls -1 $redTP53Path | tr "\\n" "\\n" > $currentPath"/reduced_tp53.txt"

mapfile -t cancerArray < reduced_cancers.txt
mapfile -t tp53Array < reduced_tp53.txt

rm "reduced_cancers.txt"
rm "reduced_tp53.txt"

cancerCount=${#cancerArray[@]}
tpCount=${#tp53Array[@]}

for i in `seq 0 $(($tpCount - 1))`
do
    for can in `seq 0 $(($cancerCount - 1))`
    do
        if [[ ${cancerArray[can]} =~ $regex ]]
        then
            canRegex="${BASH_REMATCH[1]}"
            if [[ ${tp53Array[i]} =~ $regex ]]
            then
                tpRegex="${BASH_REMATCH[1]}"
                if [[ $tpRegex == $canRegex ]]
                then
                    echo ${tp53Array[i]} ${cancerArray[can]}
                    python $scriptsPath$analyse $redTP53Path${tp53Array[i]} $redCancerPath${cancerArray[can]} >> $outFile
                fi    
            fi
        fi
    done
done

echo Sorting
python $scriptsPath$pysort $outFile
chmod 777 $outFile
chown :22257 $outFile
