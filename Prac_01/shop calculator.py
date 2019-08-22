number_of_items = int(input("Number of items:"))
total_price = 0
discount = .1
while number_of_items <= 0:
    number_of_items = int(input("Invalid. Please enter again:"))
for i in range(number_of_items):
    price_of_item = float(input("Please enter item price:"))
    if price_of_item > 100:
        price_of_item = price_of_item - price_of_item * discount
    total_price += price_of_item
print("Total price for 3 items {} is ${:.2f}".format(number_of_items, total_price))
