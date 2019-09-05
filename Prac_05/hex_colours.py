COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "beige": "#f5f5dc", "black": "#000000"}

selected_colour = input("Please enter a colour you would like to know the code of:")
while selected_colour != "":
    if selected_colour in COLOUR_NAMES:
        print(COLOUR_NAMES[selected_colour])
    else:
        print("Invalid colour")
    selected_colour = input("Please enter a colour you would like to know the code of:")