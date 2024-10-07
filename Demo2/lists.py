# Lists are data structures that comtains an odered lsit of elements.
# order means they can be accessed by an index

# use square brackets for lists
games = ["Rocket League",
         "Titan Fall 2",
         "Rainbow 6",
         "Halo 3",
         "Keanu's Blackjack",
         "That stupid Terraria",
         "Roblox - a bunch",
         "Mario Party",
         "Mario Kart (SNES)"
         ]


high_scores = [2, 7, 5, 9]
mixed_list = ["Mr, Klins", 43, True]
list_of_list = [{"Rocket League", 2},
                {"Titan Fall 2", 7},
                {"Rainbow 6", 5},
                {"Halo 3", 9}
                ]


# access element by index
print(games[2])
# access element from bacl of list
print(games[-1])

# changing values in a list
games[-1] = "Garfield Kart"
print(games)

# slicing lists:
# a slice is a subset of a list
first_four = games[:4]
print(first_four)

last_four = games[-4:]  # remember we changed the last one to garfield
print(last_four)

middle_slice = games[4:6]
print(middle_slice)

# create a lsit of numbers
numbers = list(range(10))
print(numbers)
# print every other numbers
print(numbers[::2])
print(numbers[1:7:2])
# prints every third numbers Ex: 3,6,9,ect;
print(numbers[::3])

# reverse a list
print(numbers[::-1])

# combining lists
combined = games + high_scores
print(combined)

# repeating lists
repeated = [5] * 10
print(repeated)
duplicated_high_scores = high_scores * 2
print(duplicated_high_scores)

# find the lenght of a list
print(len(high_scores))
print(len(duplicated_high_scores))

# unpacking a list
name, age, likes_teaching = mixed_list
print(f"{name} {age} {likes_teaching}")

# unpacking with a remainder 8 (first, middle_chunk, last)
game1, *other_games, game2 = games
print(f"{game1} {other_games} {game2}")

# iterate through a list
for i in games:
    print(i)

# iterate through a list, but also know the index USE ENUMERATE
for index, game in enumerate(games):
    print(f"{index}: {game}")

# adding items to a list
# append method
games.append("Odie Role Play")
print(games)
# insert item to list:
games.insert(1, "John Abuckle's night on the town")
print(games)

# removing elements
games.remove("Halo 3")
print(games)

# remove the last element
games.pop()
print(games)

# removes a specific index
games.pop(3)
print(games)

# find the index of a element
print(games.index("John Abuckle's night on the town"))

# note, you'll get an error if the element doesn't exist:
# this makes it crash ---> print(games.index("Odie Role Play"))
# Value error: 'Odie Role Play' is not in lsit

# to avoid value error:
if "Odie Role Play" in games:
    print(games.index("Odie Role Play"))
else:
    print("What have you done with Odie")

# sorts lists
nums_to_sort = [6, 4, 5, 1, 9]
print(nums_to_sort)
nums_to_sort.sort()  # sorting in place - updating order of current list
print(nums_to_sort)
# nums_to_sort.reverse=True) # this will reverse the sort
nums_to_sort.sort(reverse=True)
print(nums_to_sort)

# create a new sorted lsi without editing the existing one:
new_nums_to_sort = sorted(nums_to_sort)
print(nums_to_sort)  # should be in reverse
print(new_nums_to_sort)  # should be sorted normaly
