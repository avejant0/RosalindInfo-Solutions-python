def main():
    f_input = open('input.txt','r');
    sequences = f_input.readlines();
    f_input.close();
    hammdistance = 0
    for i in range(0,len(sequences[0])-1):
        if sequences[0][i] != sequences[1][i]:
            hammdistance += 1;
    f_out = open('output.txt','w')
    f_out.write(str(hammdistance))
    f_out.close()
    
main()