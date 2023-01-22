n = int(input())
if 1 <= n <= 100 and n%2!=0:
    m=n//2+1  #3
    for i in range(1,n+1):    
        if i <=m:
            print((m-i+1)*"*\t",end="")
            print((2*i-1)*"\t",end="")
            print((m-i+1)*"*\t")
        else:
            print((i-m+1)*"*\t",end="")
            print((2*(n-i)+1)*"\t",end="")
            print((i-m+1)*"*\t")
