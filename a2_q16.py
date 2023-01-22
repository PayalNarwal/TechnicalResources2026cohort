n = int(input())
if 1 <= n <= 100 :
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="\t")
        for k in range(1,2*(n-i)):
            print("\t",end="")
        temp = i
        if i<n:
            for l in range(1,i+1):
                print(temp,end="\t")
                temp-=1
        else:
            for l in range(1,i):
                temp-=1
                print(temp,end="\t")
        print()
