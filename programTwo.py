seqFile = open('expression.txt', 'r')

# Creating two empty Lists "gene and expression"
gene = []
expression = []

# For loop to extract columns from the file and put(append()) them into the Lists(gene, expression)
for line in seqFile:
    gene.append(line.split("\t")[0].strip())
    expression.append(line.split("\t")[1].strip())

# Assigning strings(custom genes) to look for inside the lists
geneA = "BRCA1"
geneB = "JAK2"
geneC = "KRAS"

print "Genes","  ", "Expression_count"
print "------"," ", "----------------"

# printing out the gene name and expression count
for x in gene:
    if x == geneA:
        print geneA," : ", expression[gene.index(geneA)]
    elif x == geneB:
        print geneB," : ", expression[gene.index(geneB)]
    elif x == geneC:
        print geneC," : ", expression[gene.index(geneC)]
