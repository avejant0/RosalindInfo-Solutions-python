def main():
    f_input = open('input.txt','r');
    line = f_input.read();
    f_input.close();
    numbers = line.split();
    AAAA = float(numbers[0]);
    AAAa = float(numbers[1]);
    AAaa = float(numbers[2]);
    AaAa = float(numbers[3]);
    Aaaa = float(numbers[4]);
    aaaa = float(numbers[5]);
    expectedValue = 2*(AAAA+AAAa+AAaa+0.75*AaAa + 0.5*Aaaa);
    f_output = open('output.txt','w');
    f_output.write(str(expectedValue));
    f_output.close();
main();
