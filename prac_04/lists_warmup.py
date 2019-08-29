numbers = [3, 1, 4, 1, 5, 9, 2]
# [0] = 3    [-1] = 2    [3] = 1   [:-1] = 3,1,4,1,5,9   [3:4] = 1    5 in numbers = true   7 in numbers = false
# "3" in numbers = false     numbers + [6, 5, 3]  = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
check = "3" in numbers
print(check)
print(numbers + [6, 5, 3])

numbers[0] = 10
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)
