import sys
sys.path.insert(0, '../_common');

import bioinf

def main():
    f_input = open('input.txt', 'r')
    dna = f_input.read()
    f_input.close();
    rna = bioinf.transcript(dna);
    f_output = open('output.txt','w');
    f_output.write(rna);
    f_output.close();

main();