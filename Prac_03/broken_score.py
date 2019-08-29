"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    grade_calculation(score)

def grade_calculation(score):
    if score < 0 or score > 100:
        print("That's invalid")
    elif score >= 90:
        print("excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("bad")
main()
