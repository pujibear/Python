'''
Homework7
Name: Bryan Cruz
github link: 
'''


def fizzbuzz(num):
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
    return 

def scholarship_eligibility(gpa,credits):
    if gpa >= 3.5 and credits >= 60:
        print("True")
    else:
        print("False")
    
    return

def max_of_three_numbers(num1,num2,num3):
    a = num1
    b = num2
    c = num3
    
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest7.py'))