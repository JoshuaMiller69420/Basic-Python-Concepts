num_1 = int(input("Input number: "))
num_2 = int(input("Input number: "))
num_3 = int(input("Input number: "))


if num_1 == num_2 and num_3:
    print("Equilateral")
elif num_1 == num_2 and num_1 == num_3 and num_3 == num_1 and num_3 == num_2 and num_2 != num_3 and num_2 != num_1:
    print("Isosceles")
elif num_1 == num_2 and num_1 == num_3 and num_3 != num_1 and num_3 != num_2 and num_2 != num_3 and num_2 != num_1:
    print("Scalene")
