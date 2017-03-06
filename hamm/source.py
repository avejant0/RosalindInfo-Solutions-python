import sys
sys.path.insert(0, '../_common');

import bioinf

def main():
    f_input = open('input.txt','r');
    sequences = f_input.readlines();
    f_input.close();
    hammdistance = bioinf.evaluateHammDistance(sequences);
    f_out = open('output.txt','w')
    f_out.write(str(hammdistance))
    f_out.close()
    
main()