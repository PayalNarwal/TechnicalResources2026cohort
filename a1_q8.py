n = int(input())     
k = int(input())    
if 1 <= n < 10**9 and -10**9 < k < 10**9 :
    r = 0
    c = len(str(n))
    if k <0:
        k = k+c
    k=k%c
    d = 10**k
    m = 10**(c-k)
    r = n//d + (n%d)*m
    print(r)
