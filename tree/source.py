def findAreasCount(nodeCount, adjList):
    areasList = range(1, nodeCount + 1);
    for item in adjList:
        valueOfEnd = areasList[item[1]-1];
        areasList = [areasList[item[0]-1] if x==valueOfEnd else x for x in areasList]
    list.sort(areasList);
    return len(list(set(areasList)));

def main():
    f_input = open('input.txt','r');
    input_list = f_input.readlines();
    f_input.close();
    nodeCount = int(input_list[0]);
    input_list = input_list[1:];
    adjacencyList = [];
    for item in input_list:
        splittedLine = item.split();
        adjacencyList.append([int(splittedLine[0]), int(splittedLine[1])]);
    areasCount = findAreasCount(nodeCount, adjacencyList);
    edgeCount = areasCount - 1;
    f_ouput = open('output.txt','w');
    f_ouput.write(str(edgeCount));
    f_ouput.close();
        
main();