
def main():
    f_input = open('input.txt', 'r');
    gc_list = [];
    currentSequenceName = '';
    for line in f_input:
        if line[0] == '>':
            if currentSequenceName!='':
                gc_list.append(currentSequence)
            currentSequenceName = line[1:-1]
            currentSequence = ''
        else:
            currentSequence+=line[0:-1]
    f_input.close();
    print gc_list;

main();