import urllib2, re

def getProteinSequence(proteinName):
    url = 'http://www.uniprot.org/uniprot/'+ proteinName + '.fasta';
    response = urllib2.urlopen(url);   
    html = response.read();
    lines = html.split('\n')[1:];
    protein = '';
    for line in lines:
        protein += line.replace('\n','').replace(' ','');
    return protein;

def main():
    f_input = open('input.txt','r');
    f_output = open('output.txt','w');
    nGlicTemplate = r'(?=(N[^P][ST][^P]))'; 
    for line in f_input:
        line = line.replace('\n','');
        protein = getProteinSequence(line);
        regExp = re.compile(nGlicTemplate);
        positions = [];
        for result in regExp.finditer(protein):
            positions.append(str(result.start()+1));
        if(len(positions)!=0):
            f_output.write(line + '\n');
            f_output.write(' '.join(positions)+'\n');
    f_input.close();
    f_output.close();

main();