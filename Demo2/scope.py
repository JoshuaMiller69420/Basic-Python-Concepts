message = ""  # this is a global variable, and a practice we will avoid doing


def greet(name):
    global message
    message = "Hello" + name
    print(message)


def greet_another(name):
    message = "Hola" + name
    print(message)


greet("Matthew Burnham")
print(message)
