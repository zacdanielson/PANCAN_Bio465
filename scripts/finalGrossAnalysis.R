library(readr)

args <- commandArgs(TRUE)

if (length(args) != 1) {
    stop("At least one argument is needed(hnsc_3p line).",call.=FALSE)
}

hnsc_3ps <- read_tsv(args[1])

our_combo <- hnsc_3ps[1,5]
our_ncombo <- hnsc_3ps[1,6]

gross_combo <- hnsc_3ps[2,5]
gross_ncombos <- hnsc_3ps[2,6]

cTable <- rbind(c(our_combo, our_ncombo), c(gross_combo, gross_ncombos))
fisherResult <- fisher.test(cTable)
fisherPValue <- fisherResult$p.value

print( fisherPValue )


