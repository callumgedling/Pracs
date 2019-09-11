from Prac_06.guitars import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
other_guitar = Guitar("Another guitar", 2012, 295751)

# print(gibson)
# print("{} get_age() - Expected 96, got {}".format(gibson.name, gibson.get_age()))
# print("{} get_age() - Expected 7, got  {}".format(other_guitar.name, other_guitar.get_age()))
# print("{} is_vintage()- Expected True, got {}".format(gibson.name, gibson.is_vintage()))
# print("{} is_vintage()- Expected False, got {}".format(other_guitar.name, other_guitar.is_vintage()))

guitars = [gibson, other_guitar]

print("My guitars!")
name = input("Name:")
while name != "":
    year = int(input("Year:"))
    cost = int(input("Cost:"))
    print("{} ({}) : ${} has been added.".format(name, year, cost))
    guitar_to_add = Guitar(name, year, cost)
    guitars.append(guitar_to_add)
    name = input("Name:")

print("...snip...")
print("These are my guitars:")
for i, guitar in enumerate(guitars):
    vintage_string = ""
    if guitar.is_vintage:
        vintage_string = "(vintage)"
    print("Guitar {}: {} {}".format(i + 1, guitar, vintage_string))
