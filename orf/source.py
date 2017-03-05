def readCodonTable(path):
    codonDict = {}
    f_table = open(path, 'r');
    for line in f_table:
        lineParts = line.split();
        for i in range(0,len(lineParts)-1):
            if i % 2 ==0:
                codonDict[lineParts[i]] = lineParts[i+1];
    f_table.close();
    return codonDict;

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
    
def getORFList(rna, reversedRna, codonTable, startCodon, startCodonPosition,startCodonPositionForReversed):
    orfList = [];
    for position in startCodonPosition:
        currentProtein = '';
        for i in range(position, len(rna), 3):
            if(len(rna)-1 < i+2):
                break;
            currentCodon = rna[i] + rna[i+1] + rna[i+2];
            if codonTable[currentCodon] != 'Stop':
                currentProtein += codonTable[currentCodon];
            else:
                if currentProtein not in orfList:
                    orfList.append(currentProtein);
                break;

    for position in startCodonPositionForReversed:
        currentProtein = '';
        for i in range(position, len(reversedRna), 3):
            if(len(reversedRna)-1 < i+2):
                break;
            currentCodon = reversedRna[i] + reversedRna[i+1] + reversedRna[i+2];
            if codonTable[currentCodon] != 'Stop':
                currentProtein += codonTable[currentCodon];
            else:
                if currentProtein not in orfList:
                    orfList.append(currentProtein);
                break;

    return orfList;
                
def getComplementOfRna(rna):
    complRule = {'A':'U', 'U':'A', 'G':'C', 'C':'G'};
    complementRna = '';
    for i in range(0,len(rna)):
        complementRna += complRule[rna[i]];
    return complementRna;              

def main():
    codonTableResults = readCodonTable('codon_table.dat');
    codonTable = codonTableResults;
    startCodon = 'AUG';
    f_input = open('input.txt','r');
    dna = '';
    for line in f_input:
        if(line[0]!='>'):
            dna+=line[0:-1];
    f_input.close();
    rna = transcript(dna);
    reversedRna = getComplementOfRna(rna[::-1]);
    startCodonPosition = findAllStartCodonPositions(rna, startCodon);
    startCodonPositionForReversed= findAllStartCodonPositions(reversedRna, startCodon);
    orfList = getORFList(rna,reversedRna, codonTable, startCodon, startCodonPosition, startCodonPositionForReversed );
    f_output = open('output.txt','w');
    for line in orfList:
        f_output.write(line + '\n');
    f_output.close();

main();