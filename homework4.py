'''
Homework4
Name: Bryan Cruz
github link:
'''

def grade_calculator(score):
    #I had to write all grades in so i can put the limits on each side
    if score > 100:
        print("'Enter a grade between 0-100'")
    elif score >= 90:
        print("'A'")
    elif score >= 80:
        print("'B'")
    elif score >= 70:
        print("'C'")
    elif score >= 60:
        print("'D'") 
    elif score >= 0:
        print("'F'")
    else:
        print("'Enter a grade between 0-100'")
    return

def even_or_odd(num):
    if num % 2:
        print("'odd'")
    else:
        print("'even'")
    
    return 



if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest4.py'))