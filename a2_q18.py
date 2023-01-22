n = int(input())
if 1 <= n <= 100 and n%2!=0:
    m=n//2 #3
    for i in range(1,n+1):
        if i==1:
            print("*\t"*n,end="")
        elif i>m:
            print("\t"*(n-i),end="")
            print("*\t"*(2*(i-m)-1),end="")
        else:
            print("\t"*(i-1),end="")
            print("*\t",end="")
            print("\t"*(2*(m-i)+1),end="")
            print("*\t",end="")
        print()
