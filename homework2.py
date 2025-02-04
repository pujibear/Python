'''
Homework2
Name:Bryan Cruz
github link: 
'''

def inches_to_cm(inches):
    conversions = 2.54
    inches_to_cm = inches * conversions
    print(f"{inches_to_cm:.2f}")
    return 

def feet_to_meters(feet):
    cmeters = 0.3048
    feet_to_meters = feet * cmeters
    print(f"{feet_to_meters:.2f}")
    return 

def lbs_to_kg(lbs):
    ckg = 2.20462
    lbs_to_kg = lbs / ckg
    print(f"{lbs_to_kg:.2f}")
    return 

def hours_to_minutes(hrs):
    cmin = 60
    hours_to_minutes = hrs *cmin
    print(f"{hours_to_minutes:.1f}")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))