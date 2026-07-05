import random

# A list of 5 words to guess
WORDS = ["python", "keyboard", "hangman", "program", "developer"]

# A list of hints — same order as WORDS
HINTS = [
    "A popular programming language",
    "You type on this",
    "The name of this game",
    "A set of instructions for a computer",
    "Someone who writes code",
]

# A list of hangman drawings (7 stages: 0 wrong → 6 wrong)
HANGMAN = [
    """
    -----
    |   |
        |
        |
        |
    =====""",
    """
    -----
    |   |
    O   |
        |
        |
    =====""",
    """
    -----
    |   |
    O   |
    |   |
        |
    =====""",
    r"""
    -----
    |   |
    O   |
   /|   |
        |
    =====""",
    r"""
    -----
    |   |
    O   |
   /|\  |
        |
    =====""",
    r"""
    -----
    |   |
    O   |
   /|\  |
   /    |
    =====""",
    r"""
    -----
    |   |
    O   |
   /|\  |
   / \  |
    =====""",
]

# FUNCTION 1 — Pick a random word and its hint

def choose_word():
    index = random.randint(0, len(WORDS) - 1)  # random index from list
    return WORDS[index], HINTS[index]           # return both word and hint


# FUNCTION 2 — Show the word with blanks for unguessed letters

def show_word(word, guessed):
    display = []                  # empty list to build the display
    for letter in word:           # loop through each letter in the word string
        if letter in guessed:     # if player already guessed this letter
            display.append(letter)    # show the letter
        else:
            display.append("_")       # hide it with a blank
    return "  ".join(display)     # join list into a string like "p  _  t  _  o  n"



# FUNCTION 3 — Check if the player has guessed all letters

def is_won(word, guessed):
    for letter in word:           # check every letter in the word string
        if letter not in guessed: # if any letter is still missing
            return False
    return True                   # all letters found — player wins



# FUNCTION 4 — Ask for a valid letter that hasn't been guessed yet

def get_guess(guessed):
    while True:
        guess = input("  Guess a letter : ").strip().lower()

        if len(guess) != 1:
            print("  Please enter just one letter.\n")
        elif not guess.isalpha():
            print("  Only letters are allowed.\n")
        elif guess in guessed:    # check if letter is already in the guessed list
            print(f"  You already tried '{guess}'. Pick another.\n")
        else:
            return guess          # valid letter — return it


# FUNCTION 5 — Run one full round of the game

def play():
    word, hint = choose_word()    # get a random word and hint

    guessed = []                  # list to store every letter the player tries
    wrong   = 0                   # wrong guess counter
    limit   = 6                   # max wrong guesses

    print(f"\n  Hint   : {hint}")
    print(f"  Length : {len(word)} letters\n")  # use string len() to show word length

    while wrong < limit:

        print(HANGMAN[wrong])     # print the drawing from the list using wrong as index

        # Build and show the word progress using our string
        print(f"\n  Word    : {show_word(word, guessed)}")
        print(f"  Wrong   : {wrong} / {limit}")

        # Build a list of only the wrong guesses to display
        wrong_list = [l for l in guessed if l not in word]
        print(f"  Missed  : {', '.join(wrong_list) if wrong_list else 'None'}")
        print("-" * 40)

        if is_won(word, guessed):
            print(f"  You won! The word was '{word.upper()}'\n")
            return

        guess = get_guess(guessed)
        guessed.append(guess)     # add the new guess to the list

        if guess in word:         # check if guess is inside the word string
            times = word.count(guess)   # count how many times it appears
            print(f"\n  '{guess}' is in the word ({times} time/s)!\n")
        else:
            wrong += 1
            print(f"\n  '{guess}' is not in the word. {limit - wrong} left.\n")

    # Player ran out of guesses
    print(HANGMAN[limit])
    print(f"\n  Game over! The word was '{word.upper()}'\n")

    # Show letters the player got right using a list
    correct = [l for l in guessed if l in word]
    print(f"  Letters you got right : {', '.join(correct) if correct else 'None'}\n")


 MAIN — run the game, ask to play again

print("=" * 40)
print("     HANGMAN — Word Guessing Game")
print("=" * 40)

while True:
    play()
    again = input("  Play again? (yes / no) : ").strip().lower()
    if again not in ("yes", "y"):
        print("\n  Thanks for playing! Goodbye.\n")
        break
