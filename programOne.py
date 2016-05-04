# Use "open()" function to open the "sequence.fasta" file and assign it to seqFile
f = open('sequence.fasta', 'r')

# Creating the following variablesr to be used later
Cytocine = 0
Guanine = 0
Adinine = 0
Thymine = 0

# Using "FOR loop" to extract line by line from the file
for line in f:
    if not line.startswith(">"):
        Cytocine = Cytocine+line.count("C")
        Guanine = Guanine+line.count("G")
        Adinine = Adinine+line.count("A")
        Thymine = Thymine+line.count("T")

# Using "print" function to print an output
print "Guanine + Cytocine = ",Cytocine+Guanine
print "Adinine + Thymine = ",Adinine+Thymine
print "Total: ", Cytocine+Guanine+Adinine+Thymine
print "GC ratio:  ",(Cytocine+Guanine)/float(Cytocine+Guanine+Adinine+Thymine)
