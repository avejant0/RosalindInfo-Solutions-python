def main():
    f_input = open('input.txt','r');
    input_str = f_input.read()[0:-1];
    input_numbers = input_str.split()
    f_input.close();
    k = 2;m = 2;n = 2;
    # k = int(input_numbers[0]);
    # m = int(input_numbers[1]);
    # n = int(input_numbers[2]);
    total = k + m + n;
    recessive = 0;
    dominant = total - recessive;


main();