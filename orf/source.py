import sys
sys.path.insert(0, '../_common');

import bioinf
      
def main():
    codonTablePath = '../_refData/codon_table.dat';
    codonTable = bioinf.readCodonTable(codonTablePath);
    f_input = open('input.txt','r');
    dna = '';
    for line in f_input:
        if(line[0]!='>'):
            dna+=line[0:-1];
    f_input.close();
    rna = bioinf.transcript(dna);
    reversedRna = bioinf.getComplementOfRna(rna[::-1]);
    startCodonPosition = bioinf.findAllStartCodonPositions(rna);
    startCodonPositionForReversed= bioinf.findAllStartCodonPositions(reversedRna);
    orfList = bioinf.findOpenReadingFrames(rna,reversedRna, codonTable, startCodonPosition, startCodonPositionForReversed );
    f_output = open('output.txt','w');
    for line in orfList:
        f_output.write(line + '\n');
    f_output.close();

main();