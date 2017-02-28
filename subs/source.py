def findMotif(sequence, motif):
    motif_locations = [];
    i = 0;
    while(i<len(sequence)):
        index = sequence.find(motif,i);
        if index != -1:
            i=index;
            motif_locations.append(str(index+1));
        i+=1;
    return ' '.join(motif_locations);

def main():
    f_input = open('input.txt','r');
    sequences = f_input.readlines();
    sequence = sequences[0][0:-1];
    motif = sequences[1][0:-1];
    f_input.close();
    output = findMotif(sequence, motif);
    f_output = open('output.txt','w');
    f_output.write(output);
    f_output.close();
main();