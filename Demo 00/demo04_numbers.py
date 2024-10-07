import math
my_int = 5
my_other_int = 10
print("Maths!!!!!")
print("Addition: 5 + 6 = ", +  int(5 + 6))
print(f"Addition: 5 + 6 = {5+6}")
print(f"Value of my_intt: {my_int}")
sum = my_int + my_other_int
print(f"{my_int} + {my_other_int} = {sum}")
differnce = my_other_int - my_int
print(f"{my_other_int} - {my_int} = {differnce}")
product = my_int*my_other_int
print(f"{my_int}*{my_other_int}={product}")
quotient = my_other_int/my_int
print(f"{my_other_int}/{my_int}={quotient}")
remainder = my_other_int % my_int
print(f"{my_other_int}%{my_int}={remainder}")
int_div_quotient = my_other_int // my_int
print(f"{my_other_int}//{my_int}={int_div_quotient}")
power_result = my_other_int ** my_int
print(f"{my_other_int}**{my_int}={power_result}")

print(type(sum))
print(type(differnce))
print(type(product))
print(type(quotient))


# add 5 to my int
# my_int = my_int+5
my_int += 5  # same as above. Also works with the other operators
print(my_int)


print(f"5.7 rounded: {round(5.7)}")
print(f"5.2 rounded: {round(5.2)}")
print(f"Absolute Value of -12.3 {abs(-12.3)}")
print(f"The ceiling of 14.2:{math.ceil(14.2)}")
print(f"The ceiling of 14.8:{math.floor(14.8)}")
