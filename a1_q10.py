def is_prime(n):
    p= 2
    flag = True
    while p<n:
        if n%p==0:
            flag = False
            break
        p = p+1
    return flag
n = int(input())
if 2 <= n < 10 ** 9 :
    i = 2
    while i<=n:
        if n%i==0 and is_prime(i)==True:
            print(i,end=" ")   
            n = n//i 
        else:
            i+=1
