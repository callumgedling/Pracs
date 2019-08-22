user_name = input("Please enter your name:")
OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, "w")
print(user_name, file=out_file)
out_file.close()

with open(OUTPUT_FILE, "r") as out_file:
    name = out_file.read().strip()
print("Your name is", name)


IN_FILE = "numbers.txt"
in_file = open(IN_FILE, "w")
in_file.write("17 \n 42 \n 64 \n 74")
in_file.close()

in_file = open(IN_FILE, "r")
number_one = int(in_file.readline())
number_two = int(in_file.readline())
in_file.close()
print(number_one + number_two)

in_file = open(IN_FILE, "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)

