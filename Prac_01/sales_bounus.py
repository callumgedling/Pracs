"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
user_sales = 1
while user_sales >= 0:
    user_sales = int(input("Please enter your sales:"))
    if user_sales < 1000:
        bonus = user_sales * 0.1
    else:
        bonus = user_sales * 0.15
    print("Your bonus is $", bonus)
