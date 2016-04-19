library(readr)

args <- commandArgs(TRUE)

if (length(args)!=3) {
  stop("At least three argument must be supplied (cancerpatient_file1, analysis_file2, output_file).", call.=FALSE)
} 

patient_overlap <- read_tsv(args[1])
analysis_file <- read_tsv(args[2])

patient_analysis <- NULL
#print(patient_overlap[,1:2])
patient_colnames <- c("CancerType", "TotalIndividuals", "IndividualsWithout")
for(i in 1:nrow(patient_overlap)) {
    cancer_type <- patient_overlap[i,1]
    for(j in 1:nrow(analysis_file)) {
	if (analysis_file[j,2] == cancer_type) {
	    patient_analysis <- rbind(patient_analysis, c(patient_overlap[i,1:2], analysis_file[j,7]-patient_overlap[i,2]))
	    break
	}	
    }
}
colnames(patient_analysis) <- patient_colnames
write.table(patient_analysis, file=args[3], sep="\t", row.names=F, quote=F)
