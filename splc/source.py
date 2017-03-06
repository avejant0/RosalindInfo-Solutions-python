def readCodonTable(path):
    codonDict = {}
    f_table = open(path, 'r');
    for line in f_table:
        lineParts = line.split();
        for i in range(0,len(lineParts)-1):
            if i % 2 ==0:
                codonDict[lineParts[i]] = lineParts[i+1];
    f_table.close();
    return codonDict;

def splice(sequence, intronsList):
    result = sequence;
    for intronSequence in intronsList:
        result = result.replace(intronSequence,'');
    return result;
    
def translate(sequence, codonTable):
    resultSequence = '';
    for i in range(0,len(sequence),3):
        triplet = sequence[i] + sequence[i+1] + sequence[i+2]
        if codonTable[triplet]!='Stop':
            resultSequence += codonTable[triplet];
    return resultSequence

def transcript(dna):
    return dna.replace('T','U');

def main():
    codonTable = readCodonTable('codon_table.dat');
    f_input = open('input.txt','r');
    dna_list = [];
    currentSequenceName = '';
    for line in f_input:
        if line[0] == '>':
            if currentSequenceName!='':
                dna_list.append(currentSequence);
            currentSequenceName = line[1:-1]
            currentSequence = ''
        else:
            currentSequence+=line[0:-1]
    else:
        dna_list.append(currentSequence)
    f_input.close();
    dna = dna_list[0];
    intronsList = dna_list[1:];
    splicedDna = splice(dna, intronsList);
    rna = transcript(splicedDna);
    protein = translate(rna, codonTable);
    f_output = open('output.txt','w');
    f_output.write(protein);
    f_output.close();

main();