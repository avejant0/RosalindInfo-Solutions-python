import sys
sys.path.insert(0, '../_common');

import bioinf

def main():
    f_input = open('input.txt', 'r')
    dna = f_input.read().replace('\n','');
    f_input.close();
    quantity = bioinf.nucleotidesQuantityInDna(dna);
    output_str = str(quantity['A']) + ' ' + str(quantity['C']) + ' ' + str(quantity['G']) + ' ' + str(quantity['T'])
    f_output = open('output.txt','w');
    f_output.write(output_str);
    f_output.close();

main();