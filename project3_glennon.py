import string

def dna_code(DNA_string):
    DNA = list(DNA_string)

#swap all dna parts to mirror parts
    
    for i in range(0, len(DNA)):
        if DNA[i] == "G":
            DNA[i] =  "C"
        elif DNA[i] == "C":
            DNA[i] = "G"
        elif DNA[i] == "A":
            DNA[i] = "T"
        elif DNA[i] == "T":
            DNA[i] = "A"
    
    return(DNA)

x = "ATGCTAGGAACTA"
print(dna_code(x))


def dna_code2(DNA_string2):
    DNA2 = list(DNA_string2)
    reverse = DNA2[::-1]

    return(reverse)

y = "ATGCGTCAG"
print(dna_code2(y))
   
    
