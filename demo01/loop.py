user_in = ""
while not user_in in ["1", "2"]:
    user_in = input("Enter 1 or 2 > ").strip()
print("Thank you")
print(user_in)


num = 100
while num > 0:
    print(num)
    num //= 2
