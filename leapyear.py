var = input('Input - ')

if var % 4:
    print('Output - ' + str(var) + ' is not a leap year')
else:
    if var % 100:
        print('Output - ' + str(var) + ' is a leap year')
    else:
        if var % 400:
            print('Output - ' + str(var) + ' is not a leap year')
        else:
            print('Output - ' + str(var) + ' is a leap year')