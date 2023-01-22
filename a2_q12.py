n = int(input())
if 1 <= n <= 5 :
    a=0
    b=1
    print(a)
    #print(b,end="\t")
    for i in range(1,n):
        for j in range(1,i+2):
            print(b,end="\t")
            a,b=b,a+b
        print()
