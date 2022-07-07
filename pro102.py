from doctest import NORMALIZE_WHITESPACE


noteSpace = 0

print("This is your note space, write whatever you want on here to keep some notes ig")

while noteSpace < 200:
    noteSpace = noteSpace + 1

    guess = int(input("Enter a note: "))
    print(guess)


    if not noteSpace < 5:
        print("You Ran Out of Note Space!")