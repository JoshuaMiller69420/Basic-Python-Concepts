success = False
for num in range(3):
    print(f"attempting {num}")
    if success:
        print("We did it!")
        break
else:
    print("We tried and tried and tried and failed")

print("outside the loop")

