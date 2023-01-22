n = int(input())
if 1 <= n <= 100 and n%2!=0:
    m=n//2+1  
    for i in range(1,m+1):
        for j in range(1,m-i+1):
            print("\t",end="")
        temp = i
        for k in range(1,2*i):
            if k<=i:
                print(temp,end="\t")
                temp+=1
            else:
                temp-=1
                print(temp-1,end="\t")   
        print()
    for i in range(m+1,n+1):
        for j in range(0,i-m):
            print("\t",end="")
        temp =n-i+1
        for k in range(0,2*(n-i)+1):
            if k<=(2*(n-i)+1)//2:
                print(temp,end="\t")
                temp+=1
            else:
                temp-=1
                print(temp-1,end="\t")
        print()
