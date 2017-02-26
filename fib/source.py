def Fib(n,k):
    young = 1
    old = 0
    for x in range(1,n):
        new_young = old*k
        old += young;
        young = new_young;
        print
    return old+young;

def main():
    n = 36
    k = 5
    output = str(Fib(n,k));
    print output

main()