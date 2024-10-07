# Joshua Miller
print("Make it through the Diddy Dungeon to survive. \nUse the items nearby and around you to make it out.")


def get_valid_input(prompt, *accepted_inputs):
    while True:
        user_in = input(f"{prompt} enter one of these: {
                        accepted_inputs} > ").lower().strip()
        if user_in in accepted_inputs:
            return user_in
        else:
            print("That's an invalid input.")


def step1():
    message = "You wake up chained to the wall."
    user_in = get_valid_input(message, "", "late")
    if user_in == "in time":
        step2()
    else:
        step3()


def step2():
    print("You wake up in time and have time to do stuff")
    message = "Make breakfast after shower or no breakfast"
    user_in = get_valid_input(message, "make breakfast, no breakfast")
    if user_in == "make breakfast":
        step
    else:
        step


def step3():
    print("You wake up late and don't have a lot of time")
    message = "Take shower or no shower"
    user_in = get_valid_input(message, "take shower, no shower")
    if user_in == "take shower":
        step
    else:
        step


step1()
