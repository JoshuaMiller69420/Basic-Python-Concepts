# Joshua Miller
my_name = "Joshua Miller"
length_of_my_name = len(my_name)
print(length_of_my_name)
print("First letter: " + my_name[0])
print("Third letter: "+my_name[2])
print("The third to last letter: "+my_name[-3])

# let's get a substring:
first_name = my_name[0:5]  # takes char 0-4
print(first_name)
last_name = my_name[6:8]  # takes everything from char 6 on
print(last_name)
first_two_of_last = my_name[6:8]
print(first_two_of_last)
print("\nESCAPE CHARACTERS!\n")
print("There is a  tab between tab->\t<-tab this")
print("double quotes! \"\" ")
print("slash -> \\")
print("new line.\nThis text will be on the next line")

print("\nMore String Methods\n")
print("My name in upper case: " + my_name.upper())
print("My name in lower case: " + my_name.lower())
print("The state of my  name: " + my_name)
my_name = my_name.lower()
print("The state of my name after overwrite: " + my_name)
print("My name,in proper (title) casing: " + my_name)
print("The sate of my name: " + my_name)
long_messy_string = " some data "
print(long_messy_string)
# strip removes whitespace before and after a string
print(long_messy_string.strip())
print(long_messy_string.lstrip())
# replace substring
print(my_name.replace("joshua", "chad"))  # Note: This is case sensitive
print("The state of my name: " + my_name)
print(my_name.replace("s", "😊", ))
# returns the first index of the searched string, or -1 of not found
print(my_name.find("s"))
print("osh" in my_name)
print("osh" not in my_name)
