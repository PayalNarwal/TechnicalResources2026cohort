n = int(input())
if 1 <= n <= 100 and n%2!=0:
    m=n//2+1
    for i in range(1,n+1):
        if i == m:
            print("*\t"*n,end="")
        elif i<=m:
            print("\t"*(m-1),end="")
            print("*\t"*i,end="")
        else:
            print("\t"*(m-1),end="")
            print("*\t"*(n-i+1),end="")
        print()
