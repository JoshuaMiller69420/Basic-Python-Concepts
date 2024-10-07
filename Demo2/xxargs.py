def save_user(**user):
    print(user)  # user is a dictionary based on the args
    print(user["id"])
    print(user["name"])
    print(user["age"])


save_user(id=5, name="Tony", age=43)
