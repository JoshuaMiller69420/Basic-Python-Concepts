# Write a program the takes the test score from the user and prints a letter grade
# 90 or above = A
# 80 or above = B
# 70 or above = C
# 60 or above = D
# 59 <= YOU FAIL
# print the grade

test = int(input("Your Score:"))

if test >= 90:
    print("Your Grade: A")
elif test >= 80:
    print("Your Grade: B")
elif test >= 70:
    print("Your Grade: C")
elif test >= 60:
    print("Your Grade: D")
else:
    print("Your Grade: F")
