def createMassTableFromFile(path):
    table = {};
    file = open(path,'r');
    for line in file:
        splittedLine = line.split();
        table[splittedLine[0]] = float(splittedLine[1]);
    file.close();
    return table;

def evaluateProteinMass(protein, massTable):
    mass = 0.0;
    for i in range(0, len(protein)):
        mass += massTable[protein[i]];
    return mass;

def main():
    massTable = createMassTableFromFile('mass_table.dat');
    f_input = open('input.txt','r');
    protein = f_input.read()[0:-1];
    f_input.close();
    proteinMass = evaluateProteinMass(protein, massTable);
    f_output = open('output.txt','w');
    f_output.write(str(proteinMass));
    f_output.close();
    
main();