def max(dict):
    max_value = 0;
    max_key = '';
    for key in dict:
        if(dict[key]>max_value):
            max_value = dict[key];
            max_key = key;
    return max_key;

def createProfile(list):
    profileList = [];
    for i in range(len(list[0])):
        tmpDict = {'A':0,'G':0,'C':0,'T':0};
        for j in range(len(list)):
            tmpDict[list[j][i]]+=1;
        profileList.append(tmpDict);
    return profileList;

def findConsensus(profile):
    consensus = '';
    for i in range(0, len(profile)):
        consensus += max(profile[i]);
    return consensus;

def formatProfile(list):
    formattedDict = {'A':'','C':'', 'G':'','T':''};
    for i in range(0, len(list)):
        for key in formattedDict:
            formattedDict[key] += str(list[i][key]) + ' ';
    return formattedDict;

def main():
    f_input = open('input.txt', 'r');
    gc_list = [];
    currentSequenceName = '';
    for line in f_input:
        if line[0] == '>':
            if currentSequenceName!='':
                gc_list.append(currentSequence);
            currentSequenceName = line[1:-1]
            currentSequence = ''
        else:
            currentSequence+=line[0:-1]
    else:
        gc_list.append(currentSequence)
    f_input.close();
    profile = createProfile(gc_list);
    consensus = findConsensus(profile);
    formattedProfile = formatProfile(profile);
    f_output = open('output.txt','w');
    f_output.write(consensus + '\n');
    f_output.write('A: ' + formattedProfile['A'] + '\n');
    f_output.write('C: ' + formattedProfile['C'] + '\n');
    f_output.write('G: ' + formattedProfile['G'] + '\n');
    f_output.write('T: ' + formattedProfile['T'] + '\n');
    f_output.close();

main();