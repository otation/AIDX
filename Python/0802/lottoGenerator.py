import random

numbers = []
numbers.append(random.randint(1,45))
numbers.append(random.randint(1,45))
numbers.append(random.randint(1,45))
numbers.append(random.randint(1,45))
numbers.append(random.randint(1,45))
numbers.append(random.randint(1,45))
numbers.sort()

dFilter = []
dFilter.append(numbers.count(numbers[0]))
dFilter.append(numbers.count(numbers[1]))
dFilter.append(numbers.count(numbers[2]))
dFilter.append(numbers.count(numbers[3]))
dFilter.append(numbers.count(numbers[4]))
dFilter.append(numbers.count(numbers[5]))

print(numbers)

while sum(dFilter) != 6:
    numbers.clear()
    numbers.append(random.randint(1,45))
    numbers.append(random.randint(1,45))
    numbers.append(random.randint(1,45))
    numbers.append(random.randint(1,45))
    numbers.append(random.randint(1,45))
    numbers.append(random.randint(1,45))
    numbers.sort()  

print(numbers)