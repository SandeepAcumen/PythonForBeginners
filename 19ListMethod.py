numbers = [5,6,4,2,65]
numbers.insert(0,22)
numbers.append(11)
numbers.remove(2)
#numbers.clear()

print(4 in numbers)

print(numbers.index(65))
numbers.sort()
numbers.reverse()
print(numbers)

number2 =numbers.copy()
number2.append(123)
print(number2)

# find duplicate in list

no3 =[2,4,6,9,2]
uniques =[]
for number in no3:
    if number not in uniques:
        uniques.append(number)
print(uniques)


no4 =[2,4,6,7,2,4,]
dupli = []
for number1 in no4:
    if number1 not in dupli:
        dupli.append(number1)
print(dupli)


