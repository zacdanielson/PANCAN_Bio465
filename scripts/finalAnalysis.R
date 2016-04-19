library(readr)

args <- commandArgs(TRUE)


if (length(args)!=2) {
  stop("At least two argument must be supplied (input_file, output_file).", call.=FALSE)
} 

data10 <- read_tsv(args[1])
pValues <- c() 
count = 0
for(i in 1:1505){
    theSpecial <- c(data10[i,5], data10[i,6])
    theRest <- c((sum(data10[5])-data10[i,5]), sum(data10[6])-data10[i,6])

    cTable <- rbind(theSpecial, theRest)
    fisherResult <- fisher.test(cTable)
    fisherPValue <- fisherResult$p.value
    pValues <- rbind(pValues, fisherPValue)

}

output10 <- data10

output10["p-value"] <- pValues
output10["Bonferroni"] <- p.adjust(pValues, method = "bonferroni")
output10["FDR"] <- p.adjust(pValues, method = "fdr")

write.table(output10, file=args[2], sep="\t", row.names=F, quote=F)

