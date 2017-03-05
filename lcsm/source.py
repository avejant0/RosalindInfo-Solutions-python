def getAllSubstringsOfSize(sequence, size):
    result = [];
    for i in range(0, len(sequence)-size+1):
        result.append(sequence[i:i+size]);
    return result;

def findShortestDna(list):
    min = 100000;
    minDna = '';
    for dna in list:
        if len(dna) < min:
            min = len(dna);
            minDna = dna;
    return minDna;

def findCommonSubstring(list):
    shortestDna = findShortestDna(list);
    for i in range(len(shortestDna),0,-1):
        substrings = getAllSubstringsOfSize(shortestDna,i);
        for j in range(0, len(substrings)):
            for k in range(0,len(list)):
                if(list[k].find(substrings[j])==-1):
                    break;               
            else:
                return substrings[j];

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
    commonSubstr = findCommonSubstring(dna_list);
    f_output = open('output.txt','w');
    f_output.write(commonSubstr);
    f_output.close();

main();
    