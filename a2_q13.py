import math
n = int(input())
if 1 <= n <= 10 :
    for i in range(0,n):
        for j in range(0,i+1):
            print(math.comb(i,j),end="\t")
        print()
