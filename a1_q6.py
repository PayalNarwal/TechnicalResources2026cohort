n = int(input())
if n>=1 and n<10**9:
    for i in str(n)[::-1]:
        print(i)
