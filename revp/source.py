def isReversePalindrome(sequence):
    complRule = {'A':'T','T':'A','G':'C','C':'G'};    
    mid = len(sequence)/2;
    left = sequence[0:mid];
    right = sequence[mid:];
    revLeft = ''
    for i in range(0,mid):
        revLeft = complRule[left[i]] + revLeft;
    return revLeft == right;

def main():
    f_input = open('input.txt','r');
    dna = '';
    for line in f_input:
        if line[0] != '>':
            dna+=line.replace('\n','');
    f_input.close();
    palindromList = [];
    for i in range(0, len(dna)):
        for j in range(4,13,2):
            subS = dna[i:i+j];
            if len(subS) < j:
                break;
            if isReversePalindrome(subS):
                palindromList.append(str(i+1)+' '+ str(j)+'\n');
    f_output = open('output.txt','w');
    f_output.writelines(palindromList);
    f_output.close();
main();