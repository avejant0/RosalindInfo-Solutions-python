f = open('input.txt', 'r')
output = dict.fromkeys(['A','G','T', 'C'], 0)
input_str = f.read()

for x in range(0, len(input_str)):
    output[input_str[x]] += 1

output_str = str(output['A']) + ' ' + str(output['C']) + ' ' + str(output['G']) + ' ' + str(output['T'])

print output_str