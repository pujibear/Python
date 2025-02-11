'''
Homework5
Name: Bryan Cruz
github link:
'''

def collatz_conjecture(num):
    while (num != 1):
        print(num / 1)
        if num % 2 == 0:  # Even
            num = num / 2
        else:  # Odd
            num = 3 * num + 1
    print(1.0)
    return 

def add_numbers(num):
    n = num - 1
    sum = 0

    while n > 0:
        sum = n + sum
        n -= 1
    print(sum)

    return

if __name__ == "__main__":
    # collatz_conjecture(18.0)
    import doctest
    print(doctest.testfile('doctest5.py'))