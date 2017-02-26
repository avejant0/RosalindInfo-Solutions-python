def gc_percentage(sequence):
    length = len(sequence);
    gcquantity = 0;
    for i in range(0,len(sequence)):
        if sequence[i] == 'G' or sequence[i] == 'C':
            gcquantity = gcquantity + 1;
    return 100 * float(gcquantity)/float(length)

def max(dict):
    max = 0
    maxKey=''
    for x in dict:
        if dict[x]>= max:
            maxKey = x
            max = dict[x]
    return maxKey
    

def main():
    f_input = open('input.txt', 'r');
    gc_dict = {};
    currentSequenceName = '';
    for line in f_input:
        if line[0] == '>':
            if currentSequenceName!='':
                gc_dict[currentSequenceName] = gc_percentage(currentSequence)
            currentSequenceName = line[1:-1]
            currentSequence = ''
        else:
            currentSequence+=line[0:-1]
    f_input.close();
    maximumGc = max(gc_dict);
    output_str = maximumGc + '\n' + str(gc_dict[maximumGc]);
    f_out = open('output.txt','w')
    f_out.write(output_str)
    f_out.close()

main()