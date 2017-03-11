def NarayanaNextPerm(permutation):
    n = len(permutation);
    k = n - 2;
    while (k >= 0) and (permutation[k]>=permutation[k+1]):
        k -= 1;
    if (k==-1):
        return 0;
    t = n - 1;
    while (t>=k+1) and (permutation[k] >= permutation[t]):
        t -= 1;
    tmp = permutation[k];
    permutation[k] = permutation[t];
    permutation[t] = tmp;
    i = 0;
    for i in range(k+1,((n+k)/2)+1):
        t = n + k - i;
        tmp = permutation[i];
        permutation[i] = permutation[t];
        permutation[t] = tmp;
    return i;

def main():
    f_input = open('input.txt','r');
    n = int(f_input.read());
    f_input.close();
    permList = [];
    initialPermutation = range(1,n+1);
    permList.append(' '.join(str(v) for v in initialPermutation));
    while True:
        nextPerm = NarayanaNextPerm(initialPermutation);
        if nextPerm == 0:
            break;
        permList.append(' '.join(str(v) for v in initialPermutation));
    f_output = open('output.txt','w');
    f_output.write(str(len(permList))+'\n');
    for item in permList:
        f_output.write(item + '\n');
    f_output.close();

main();