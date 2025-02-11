'''
Homework3
Name: Bryan Cruz
github link:
'''

def positive_or_negative(num):
    if num > 0:
        print("True")
    else:
        print("False")
    
    return 

def is_able_to_drive(num):
    if num >= 16:
        print("True")
    else:
        print("False")
    return

def is_able_to_vote(num):
    if num >= 18:
        print("True")
    else:
        print("False")
    return

def can_buy_alcohol(num):
    if num >= 21:
        print("True")
    else:
        print("False")  
    return 

def senior_discount(num):
    if num >= 65:
        print("True")
    else:
        print("False")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py'))