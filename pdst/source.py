import sys
sys.path.insert(0, '../_common');

import bioinf

def createZeroMatrix(n):
    matrix = [];
    for i in range(0, n):
        l = [];
        for j in range(0, n):
            l.append(float(0));
        matrix.append(l);
    return matrix;

def main():
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
    matrix = createZeroMatrix(len(dna_list));
    dnalength = len(dna_list[0]);
    listLength = len(dna_list);
    for i in range(0,listLength):
        for j in range(0,listLength):
            if i != j:
                pDistance = bioinf.evaluateHammDistance(dna_list[i], dna_list[j]) / float(dnalength);
                matrix[i][j] = pDistance;
                matrix[j][i] = pDistance;
    f_output = open('output.txt','w');
    for i in range(0,listLength):
        row = '';
        for j in range(0,listLength):
            row += str(matrix[i][j]) + ' ';
        f_output.write(row[:-1]+'\n');
    f_output.close();
    

main();