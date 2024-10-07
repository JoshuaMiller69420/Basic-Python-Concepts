import webbrowser
import random
# there are two types of functions:
# 1: perfroms a task
# 2: runs some calculationsare returns a value


# preforms a task


def who_is_john_lennon():
    print("He was a Beatle, a member of the greatest band")
    print(". . .other then Parry Gripp")


def who_is_pary_gripp():
    print("Parry Gripp is a God of Music")
    webbrowser.open("https://www.youtube.com/watch?v=EiO9_PJ0h8Q%22")

# returns a value


def get_awesome_song_link():
    links = ["https://www.youtube.com/watch?v=npjF032TDDQ",
             "https://www.youtube.com/watch?v=EiO9_PJ0h8Q",
             "https://www.youtube.com/watch?v=jcaej-i3QQo"
             ]
    return random.choice(links)


# who_is_pary_gripp()
webbrowser.open(get_awesome_song_link())
