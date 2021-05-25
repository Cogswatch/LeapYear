# import leapyear

def leapYear(year):
    if (year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0)):
        print("Output - " + str(year) + " is a leap year")
        return True
    else:
        print("Output - " + str(year) + " is not a leap year")
        return False

def test_leapyear():
    assert leapYear(1992) == True
    assert leapYear(2000) == True
    assert leapYear(1900) == False