def readCodonTable():
    codonDict = {}
    f_table = open('codon_table.txt', 'r');
    for line in f_table:
        lineParts = line.split();
        for i in range(0,len(lineParts)-1):
            if i % 2 ==0:
                codonDict[lineParts[i]] = lineParts[i+1];
    f_table.close();
    return codonDict;

def translate(sequence, codonTable):
    resultSequence = '';
    for i in range(0,len(sequence),3):
        triplet = sequence[i] + sequence[i+1] + sequence[i+2]
        if codonTable[triplet]!='Stop':
            resultSequence += codonTable[triplet];
    return resultSequence

def main():
    f_input = open('input.txt','r')
    sequence = f_input.read()[0:-1];
    f_input.close();
    codonDict = readCodonTable();
    proteinSequence = translate(sequence, codonDict);
    f_output = open('output.txt','w');
    f_output.write(proteinSequence);
    f_output.close();

main()
