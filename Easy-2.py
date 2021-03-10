def is_leap_year(year):

    if year % 400 == 0 :
        return True
    elif year % 400 != 0 and year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False

    return False

year = int(input("Input year : "))

print(f'{year} -> {is_leap_year(year)}')



