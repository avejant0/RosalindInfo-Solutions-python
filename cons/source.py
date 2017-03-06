import sys
sys.path.insert(0, '../_common');

import bioinf

def main():
    f_input = open('input.txt', 'r');
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
    profile = bioinf.createProfile(dna_list);
    consensus = bioinf.findConsensus(profile);
    formattedProfile = bioinf.formatProfile(profile);
    f_output = open('output.txt','w');
    f_output.write(consensus + '\n');
    f_output.write('A: ' + formattedProfile['A'] + '\n');
    f_output.write('C: ' + formattedProfile['C'] + '\n');
    f_output.write('G: ' + formattedProfile['G'] + '\n');
    f_output.write('T: ' + formattedProfile['T'] + '\n');
    f_output.close();

main();