
# “Years that are evenly divisible by 4 except
# years that are evenly divisible by 100
# unless the years are also evenly divisible by 400”.


# “(Years that are evenly divisible by 4) except ((years that are evenly divisible by 100) unless (the years are also evenly divisible by 400))”.

# “(Years % 4 == 0) except (years % 100 == 0) unless (years % 400 == 0)”.

# %4 | %100 | %400 | Leap Year
#  1    0       0        1
#  1    1       0        0
#  1    1       1        1

# “((Years % 4 == 0) and not (years % 100 == 0)) or (years % 400 == 0)”.

# Error Handling implementation suggested in https://docs.python.org/3/tutorial/errors.html
while True:
    try:
        year = int(input("Input - "))
        break
    except ValueError:
        print("Error! Please enter an Integer")

if (year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0)):
    print("Output - " + str(year) + " is a leap year")
else:
    print("Output - " + str(year) + " is not a leap year")