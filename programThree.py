seqFile = open('expression.txt', 'r')

# declaring an empty dictionary called "gene"
gene = {}

"""
 gene[line.split("\t")[0].strip()] <-- first column (key)
 line.split("\t")[1].strip() <-- second column (value)

 """
for line in seqFile:
    gene[line.split("\t")[0].strip()] = line.split("\t")[1].strip()

geneA = "BRCA1"

print "Expression count of gene ", geneA,"==>", gene[geneA]
