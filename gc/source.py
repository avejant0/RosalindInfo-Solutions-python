import sys
sys.path.insert(0, '../_common');

import bioinf

def main():
    f_input = open('input.txt', 'r');
    gc_dict = {};
    currentSequenceName = '';
    for line in f_input:
        if line[0] == '>':
            if currentSequenceName!='':
                gc_dict[currentSequenceName] = bioinf.gc_percentage(currentSequence)
            currentSequenceName = line[1:-1]
            currentSequence = ''
        else:
            currentSequence+=line[0:-1]
    f_input.close();
    maximumGc = bioinf.max(gc_dict);
    output_str = maximumGc + '\n' + str(gc_dict[maximumGc]);
    f_out = open('output.txt','w')
    f_out.write(output_str)
    f_out.close()

main()