def main():
    f_input = open('input.txt','r');
    input_str = f_input.read()[0:-1];
    input_numbers = input_str.split()
    f_input.close();
    k = int(input_numbers[0]);
    m = int(input_numbers[1]);
    n = int(input_numbers[2]);
    total = k + m + n;
    heteroHetero = m*(m-1);
    heteroRec = m*n;
    recRec = n*(n-1);
    recessive = (0.25*heteroHetero + heteroRec+recRec)/(total*(total-1));
    dominant = 1 - recessive;
    print dominant;

main();