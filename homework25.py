'''
Homework2
Name:  Bryan
github link: 
'''

def birthday(month,day,year):
    print("'Your birthday is " + month + " " + str(day) + ", " + str(year) + ".'")

    return 

def address(street,city,state,zipcode):
    print("'Your address is " + street + ", " + city + ", " + state + ", " + str(zipcode) + ".'")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))