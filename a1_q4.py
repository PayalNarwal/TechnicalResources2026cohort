low = int(input())
high = int(input())
if low>=2 and high < 10**6 and low<high:
    for number in range (low, high+ 1):  
        if number > 1:  
            for i in range (2, number):  
                if (number % i) == 0:  
                    break  
            else:   
                print (number) 
