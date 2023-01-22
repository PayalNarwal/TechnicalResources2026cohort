n = int(input())
if 1 <= n <= 100 and n%2!=0:
    m=n//2+1
    for i in range(1,n+1):
        if i<m:
            print("*",end="\t")
            print("\t"*(n-2),end="")
            print("*")
        else:
            for j in range(1,n+1):
                if j==1 or j==n or i==j or i+j==n+1 :
                    print("*",end="\t")
                else:
                    print("\t",end="")
            print()
