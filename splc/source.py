import sys
sys.path.insert(0, '../_common');

import bioinf
  
def main():
    codonTablePath = '../_refData/codon_table.dat';
    codonTable = bioinf.readCodonTable(codonTablePath);
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
    splicedDna = bioinf.splice(dna, intronsList);
    rna = bioinf.transcript(splicedDna);
    protein = bioinf.translate(rna, codonTable);
    f_output = open('output.txt','w');
    f_output.write(protein);
    f_output.close();

main();