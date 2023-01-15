num1 = int(input())  
num2 = int(input())  
def gcd(a,b):
    i = min(a,b)
    while i>0:
        if a%i==0 and b%i==0:
            print(i)
            break
        i-=1  
def lcm(a,b):
    i  = max(a,b)
    while True:
        if i%a==0 and i%b==0:
            print(i)
            break
        i+=1
if 2<= num1 <= 10**9 and 2<= num2 <=10**9:
    gcd(num1,num2)
    lcm(num1,num2)
