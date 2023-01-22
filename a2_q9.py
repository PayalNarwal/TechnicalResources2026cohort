n = int(input()) 
if 1 <= n <= 100 and n%2!=0 :
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==i:
                print("*",end="\t")
            elif j+i==n+1:
                print("*",end="\t")
            else:
                print("\t",end="")
        print()
