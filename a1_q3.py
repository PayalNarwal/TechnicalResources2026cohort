def is_prime(n):
    p= 2
    flag = True
    while p<n:
        if n%p==0:
            flag = False
            break
        p = p+1
    if flag == True:
        print("prime")
    else:
        print("not prime")
t = int(input())
if t>=1 and t<=10**4:
    while t>=1:
        n = int(input())
        if n>=2 and n<=10**9:
            is_prime(n)
        t-=1
