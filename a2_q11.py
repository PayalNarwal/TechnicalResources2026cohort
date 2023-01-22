n = int(input())
if 1 <= n <= 44 :
    c=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            c+=1
            print(c,end="\t")
        print()
