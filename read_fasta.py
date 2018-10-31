import sys

def read_fasta(filename):
    sequence = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            sequence = sequence + line
    f.close()
    return sequence

print(read_fasta(sys.argv[0,1]))
