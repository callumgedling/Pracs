"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    print(determine_grade(score))


def determine_grade(score):
    if score < 0 or score > 100:
        return "That's invalid"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "bad"


main()
