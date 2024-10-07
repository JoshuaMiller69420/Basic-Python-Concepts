# a function with a variable number of aguments
# num1 = 9
# num2 = 10
# num3 = 21
# print(f"{num1} + {num2} = {num3}")


def multiply(message, *numbers):
    product = 1
    print(f"{message} {numbers}")
    for num in numbers:
        product *= num
    return product


print(multiply("I'm multiplying", 2, 3, 8))
