import sys
sys.path.insert(0, '../_common');

import bioinf

def main():
    massTablePath = '../_refData/mass_table.dat';
    massTable = bioinf.readMassTableFromFile(massTablePath);
    f_input = open('input.txt','r');
    protein = f_input.read()[0:-1];
    f_input.close();
    proteinMass = bioinf.evaluateProteinMass(protein, massTable);
    f_output = open('output.txt','w');
    f_output.write(str(proteinMass));
    f_output.close();
    
main();