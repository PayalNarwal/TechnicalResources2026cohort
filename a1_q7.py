n = int(input())
c= 0
s =0
while n>0:
    c+=1
    print(c,end=",")
    r = n%10
    n =n//10
    print(r, end = ",")
    s = s + c*(10**(r-1))
    print(s)
print(s)
