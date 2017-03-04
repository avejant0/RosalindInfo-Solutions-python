def isAdjacent(node1,node2,k):
    return node1[-k:] == node2[:k];

def getOverlapGraph(nodes,k):
    adjList = [];
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i!=j:
                if(isAdjacent(nodes[i][1],nodes[j][1],k)):
                    adjList.append(nodes[i][0]+ ' ' + nodes[j][0]);
    return adjList;

def main():
    f_input = open('input.txt', 'r');
    gc_list = [];
    currentSequenceName = '';
    for line in f_input:
        if line[0] == '>':
            if currentSequenceName!='':
                gc_list.append((currentSequenceName, currentSequence));
            currentSequenceName = line[1:-1]
            currentSequence = ''
        else:
            currentSequence+=line[0:-1]
    else:
        gc_list.append((currentSequenceName, currentSequence));
    f_input.close();

    adjList = getOverlapGraph(gc_list,3);
    f_output = open('output.txt','w');
    for line in adjList:
        f_output.write(line + '\n');
    f_output.close();
main();