for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Please enter the number of stars you would like to print:"))
for i in range(number_of_stars):
    print("*", end='')

for i in range(0, number_of_stars + 1):
    print(i * "*")
