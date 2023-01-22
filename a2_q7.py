n = int(input())
if 1 <= n <= 100 :
    for i in range(1,n+1):
        for j in range(1,i):
            print("\t",end="")
        print("*")
