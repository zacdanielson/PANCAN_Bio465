#install.packages("dplyr")
library("dplyr")
library("readr")

args <- commandArgs(TRUE)

if (length(args)!=2) {
  stop("At least two argument must be supplied (input_file, output_file).", call.=FALSE)
} 

cancerTable <- read_tsv("analysis_threshold_10_sorted")
pValues <- c()
visitedCancer <- c()
for(i in 1:nrow(cancerTable)){
  if(!(cancerTable$Cancer_Type[i] %in% visitedCancer)){
    visitedCancer <- c(visitedCancer,cancerTable$Cancer_Type[i])
  
  
  
    withCancer <- cancerTable[which(cancerTable$Cancer_Type == cancerTable$Cancer_Type[i]),]
    
    withoutCancer <- cancerTable[which(cancerTable$Cancer_Type != cancerTable$Cancer_Type[i]),]
    
    special <- c(sum(withCancer$`TP53 ChrArm_event`),sum(withCancer$Non_Double_Mutation))
    
    rest <- c( sum(withoutCancer$`TP53 ChrArm_event`),sum(withoutCancer$Non_Double_Mutation))
    
    fTable <- rbind(special,rest)
    fResult <- fisher.test(fTable)
    fPValue <- fResult$p.value
    pValues <- c(pValues, fPValue)
  }
  

  
}
  fdrList <- p.adjust(pValues, method = "fdr")
  bonferroniList <- p.adjust(pValues, method = "bonferroni")
  topCancerStats <- data.frame(visitedCancer,pValues,bonferroniList,fdrList)
  names(topCancerStats)<- c("Cancer_Type","pValue","Bonferroni","FDR")
 
write.table(cancerTable, file=args[2], sep="\t", row.names=F, quote=F) 
