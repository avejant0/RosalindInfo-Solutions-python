def readCodonTable(path):
    results = [];
    codonDict = {}
    stopCodonsList = [];
    f_table = open(path, 'r');
    for line in f_table:
        lineParts = line.split();
        for i in range(0,len(lineParts)-1):
            if i % 2 ==0:
                codonDict[lineParts[i]] = lineParts[i+1];
                if(lineParts[i+1] == 'Stop'):
                    stopCodonsList.append(lineParts[i]);
    f_table.close();
    results.append(codonDict);
    results.append(stopCodonsList);
    return results;

def transcript(dna):
    return dna.replace('T','U');

def findAllStartCodonPositions(rna,startCodon):
    positions = [];
    i = 0;
    while(i<len(rna)):
        index = rna.find(startCodon,i);
        if index != -1:
            i=index;
            positions.append(index);
        i+=1;
    return positions;
    
def main():
    codonTableResults = readCodonTable('codon_table.dat');
    codonTable = codonTableResults[0];
    stopCodons = codonTableResults[1];
    startCodon = 'AUG';
    f_input = open('input.txt','r');
    dna = '';
    for line in f_input:
        if(line[0]!='>'):
            dna+=line[0:-1];
    f_input.close();
    rna = transcript(dna);
    startCodonPosition = findAllStartCodonPositions(rna, startCodon);
    print startCodonPosition;
main();