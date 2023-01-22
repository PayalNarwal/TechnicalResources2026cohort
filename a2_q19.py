n = int(input())
if 1 <= n <= 100 and n%2!=0:
    m=n//2+1 
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==m or j==m:
                print("*",end="\t")
            elif i<m:
                if i==1 and j<m:
                    print("*",end="\t")
                elif j==n:
                    print("*",end="\t")
                else:
                    print("\t",end="")
            else:
                if i==n and j>m:
                    print("*",end="\t")
                elif j==1:
                    print("*",end="\t")
                else:
                    print("\t",end="")
        print()
