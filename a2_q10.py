n = int(input()) 
if 1 <= n <= 100 and n%2!=0 :
    m=n//2+1
    for i in range(1,n+1):
        if i == 1 or i== n :
            print("\t"*(m-1),end="")
            print("*",end="")
        elif i<=m and i!=1:
            print("\t"*(m-i),end="")
            print("*\t",end="")
            print("\t"*(2*(i-1)-1),end="")
            print("*",end="")
        else:
            print("\t"*(i-m),end="")
            print("*\t",end="")
            print("\t"*(2*(n-i)-1),end="")
            print("*",end="")
        print()
