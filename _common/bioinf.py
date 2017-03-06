# this file contains often used bioinformatics methods and created for resolving problems from site http://rosalind.info by Avejant(Maria Muravyova)

# constant for start codon triplet
START_CODON = 'AUG';

# create dictionary of associations between RNA triplet and amino-acid
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

# splice introns from dna sequence
def splice(sequence, intronsList):
    result = sequence;
    for intronSequence in intronsList:
        result = result.replace(intronSequence,'');
    return result;

# translate rna to protein
def translate(sequence, codonTable):
    resultSequence = '';
    for i in range(0,len(sequence),3):
        triplet = sequence[i] + sequence[i+1] + sequence[i+2]
        if codonTable[triplet]!='Stop':
            resultSequence += codonTable[triplet];
    return resultSequence

# transcript dna to rna
def transcript(dna):
    return dna.replace('T','U');

# create profile matrix in the list of dictionary format
def createProfile(list):
    profileList = [];
    for i in range(len(list[0])):
        tmpDict = {'A':0,'G':0,'C':0,'T':0};
        for j in range(len(list)):
            tmpDict[list[j][i]]+=1;
        profileList.append(tmpDict);
    return profileList;

# find consensus from profile
def findConsensus(profile):
    consensus = '';
    for i in range(0, len(profile)):
        consensus += max(profile[i]);
    return consensus;

# format profile to human-readable table
def formatProfile(list):
    formattedDict = {'A':'','C':'', 'G':'','T':''};
    for i in range(0, len(list)):
        for key in formattedDict:
            formattedDict[key] += str(list[i][key]) + ' ';
    return formattedDict;

# get max key from dictionary
def max(dict):
    max_value = 0;
    max_key = '';
    for key in dict:
        if(dict[key]>max_value):
            max_value = dict[key];
            max_key = key;
    return max_key;

# create dictionary for quantities of each nucleotide in dna sequence
def nucleotidesQuantityInDna(dna):
    result = dict.fromkeys(['A','G','T', 'C'], 0)
    for x in range(0, len(dna)):
        result[dna[x]] += 1
    return result;

# get gc percentage of sequence
def gc_percentage(sequence):
    length = len(sequence);
    gcquantity = 0;
    for i in range(0,len(sequence)):
        if sequence[i] == 'G' or sequence[i] == 'C':
            gcquantity = gcquantity + 1;
    return 100 * float(gcquantity)/float(length)

# evaluate hamming distance for list of sequences
def evaluateHammDistance(sequences):
    hammdistance = 0
    for i in range(0,len(sequences[0])-1):
        if sequences[0][i] != sequences[1][i]:
            hammdistance += 1;
    return hammdistance;

#find all open reading frames in rna and it reversed complementary    
def findOpenReadingFrames(rna, reversedRna, codonTable, startCodonPosition,startCodonPositionForReversed):
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

# find all start codon positions in rna
def findAllStartCodonPositions(rna):
    positions = [];
    i = 0;
    while(i<len(rna)):
        index = rna.find(START_CODON,i);
        if index != -1:
            i=index;
            positions.append(index);
        i+=1;
    return positions;

# get complementary of rna
def getComplementOfRna(rna):
    complRule = {'A':'U', 'U':'A', 'G':'C', 'C':'G'};
    complementRna = '';
    for i in range(0,len(rna)):
        complementRna += complRule[rna[i]];
    return complementRna;      

# get complementary of dna
def getComplementOfDna(dna):
    complRule = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' :'G' }
    complementDna = '';
    for x in range(len(dna)-2, -1, -1):
        complementDna += complRule[dna[x]]
    return complementDna;

# read mass table from file
def readMassTableFromFile(path):
    table = {};
    file = open(path,'r');
    for line in file:
        splittedLine = line.split();
        table[splittedLine[0]] = float(splittedLine[1]);
    file.close();
    return table;

# evaluate protein mass
def evaluateProteinMass(protein, massTable):
    mass = 0.0;
    for i in range(0, len(protein)):
        mass += massTable[protein[i]];
    return mass;

# find list of motif locations in the sequence
def findMotif(sequence, motif):
    motif_locations = [];
    i = 0;
    while(i<len(sequence)):
        index = sequence.find(motif,i);
        if index != -1:
            i=index;
            motif_locations.append(str(index+1));
        i+=1;
    return motif_locations;