def Fib(n,m):
    rabbits = [0]*m;
    rabbits[0] = 1;
    for i in range(1,n):
        adults = 0;
        for j in range(1,m):
            adults += rabbits[j];
        for j in range(m-1,0,-1):
            rabbits[j] = rabbits[j-1];
        rabbits[0] = adults;
    return rabbits;

def main():
    f_input = open('input.txt','r');
    inp = f_input.read().split();
    n = int(inp[0]);
    m = int(inp[1]);
    f_input.close();
    rabbList = Fib(n,m);
    result = 0;
    for i in range(0,len(rabbList)):
        result+=rabbList[i];
    f_output = open('output.txt','w');
    f_output.write(str(result));
    f_output.close();
    
main();