f = open('input.txt', 'r')
input_str = f.read()
output_str = '';
dna_to_rna_dict = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' :'G' }
for x in range(len(input_str)-2, -1, -1):
    output_str += dna_to_rna_dict[input_str[x]]
print output_str
f_out = open('output.txt','w')
f_out.write(output_str)
f.close()
f_out.close()