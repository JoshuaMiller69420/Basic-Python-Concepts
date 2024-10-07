import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def colors():
    print("Let's play wiht colors")
    print(f"{bcolors.WARNING}warning text{bcolors.ENDC}")
    print(f"color should be reset")
    print(f"{bcolors.HEADER}warning text{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}okblue text{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}okcyan text{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}okgreen text{bcolors.ENDC}")
    print(f"{bcolors.FAIL}fail text{bcolors.ENDC}")
    print(f"{bcolors.ENDC}endc text{bcolors.ENDC}")
    print(f"{bcolors.BOLD}bold text{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}underline text{bcolors.ENDC}")


def typetext(str, end="\n"):
    for character in str:
        print(character, end="", flush=True)
        time.sleep(.1)
    print(end, end="")


def print_duck():

    typetext("I'm a bunch of text that needs printed")


def print_duck():
    print(f"{bcolors.BOLD}ASCII Art{bcolors.ENDC}")
    print(bcolors.WARNING + """
                        __
                      /` ,\__
                     |    ).-'
                    / .--'
                   / /
     ,      _.==''`  \
   .'(  _.='         |
  {   ``  _.='       /
   {    \`     ;    /
    `.   `'=..'  .='
      `=._    .='
   jgs  '-`\\`__
            `-._{""" + bcolors.ENDC)


typetext("I'm a bunch of text that needs printed")
typetext("I'm a bunch of text that needs printed")
print_duck()
