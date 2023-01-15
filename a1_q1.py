for i in range(1,6):
    if i == 1 or i == 5:
        print("*****")
    else:
        for j in range(1,6-i):
            print(" ",end="")
        print("*")
