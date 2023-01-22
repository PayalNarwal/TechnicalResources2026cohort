n = int(input())
if 1 <= n <= 100 and n%2!=0:
    m=n//2+1  
    for i in range(1,m+1):
        for j in range(1,m-i+1):
            print("\t",end="")
        for k in range(1,2*i):
            print("*",end="\t")
        print()
    for i in range(1,m):
        for j in range(1,i+1):
            print("\t",end="")
        for k in range(0,2*(m-i)-1):
            print("*",end="\t")
        print()
