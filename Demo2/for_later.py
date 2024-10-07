# write a function that prompts the user for a 1 or 2
# if the user types anything else, report the error and ask again.
# once you have a 1 or 2, return the value

# eg.
# choice = get_one_or_two()

def get_one_or_two():
    inqury = ""
    while True:
        inqury = input("1 or 2: ").strip()
        if inqury in ("1", "2"):
            return (inqury)

        print("Error")


val = get_one_or_two()
if val == "1":
    print("you died")
else:
    print("you lived")
