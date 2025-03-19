try:
    age =int(input('age:'))
    income =2000
    risk = income /age
    print(age)
except ValueError:
    print("Incorrect Input")

except ZeroDivisionError:
    print("Age can not be Zero")

