f = open('input.txt', 'r')
input_str = f.read()
output_str = ''
for x in range(0,len(input_str)):
    if input_str[x] == 'T':
        output_str += 'U'
    else:
        output_str += input_str[x]
print output_str