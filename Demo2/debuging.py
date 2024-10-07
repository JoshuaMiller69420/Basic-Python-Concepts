# click  the bug icon on the left(debuging menu)
# f9 or click to the left to add a BREAKPOINT
# f10 to step over functions
# f11 to step line by line


def multiply(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


print("Start")
print(multiply(2, 3, 4, 5))
