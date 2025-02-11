'''
Homework6
Name:
github link:
'''

def div_by_seven(num):
    for num in range(1, num + 1):    #num + 1 trying to get that last number included as well
        if num % 7 == 0:     #Trying to get the remainder
            print(num)
            
    return 

def squares_of_numbers(num):
    total = 0
    for i in range(1, num):
        total += i ** 2
        print(i ** 2)     #Trying to print every 
    
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest6.py'))