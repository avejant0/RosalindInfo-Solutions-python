import sys
sys.path.insert(0, '../_common');

import bioinf

def main():
    codonTablePath = '../_refData/codon_table.dat';
    codonTable = bioinf.readCodonTable(codonTablePath);
    f_input = open('input.txt','r')
    sequence = f_input.read()[0:-1];
    f_input.close();

    proteinSequence = bioinf.translate(sequence, codonTable);
    f_output = open('output.txt','w');
    f_output.write(proteinSequence);
    f_output.close();

main()
