import sys
sys.path.insert(0, '../_common');

import bioinf

def main():
    f_input = open('input.txt','r');
    sequences = f_input.readlines();
    sequence = sequences[0][0:-1];
    motif = sequences[1][0:-1];
    f_input.close();
    output = ' '.join(bioinf.findMotif(sequence, motif));
    f_output = open('output.txt','w');
    f_output.write(output);
    f_output.close();

main();