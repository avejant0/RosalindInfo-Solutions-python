def main():
    f_input = open('input.txt', 'r');
    l = int(f_input.read());
    f_input.close();
    i_nodes = l-2;
    f_output = open('output.txt', 'w');
    f_output.write(str(i_nodes));
    f_output.close();

main();