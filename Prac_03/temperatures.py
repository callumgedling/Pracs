"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
control alt l is the formatting shortcut
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
            fahrenheit = float(input("Fahrenheit:"))
            celsius = fahrenheit_to_clesius(celsius, fahrenheit)
            print("Result: {:.2f} c".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_clesius(celsius, fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
