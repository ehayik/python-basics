

def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = (year % 100 != 0) or (year % 400 == 0)

    return leap


print("Type year: ", end="")
prompted_year = int(input())
print("Result: {}".format(is_leap(prompted_year)))
