# Hangman — Word Guessing Game

A text-based Hangman game built with **pure Python**.  
The player guesses a hidden word one letter at a time, with a hint shown at the start, before the hangman drawing is complete.

---

## Project Info

| Detail | Info |
|---|---|
| Task | Task 1 — Hangman Game |
| Language | Python 3 |
| Libraries Used | `random` (built-in) |
| Type | Console / Terminal Application |

---

## Python Concepts Used

| Concept | Where it's applied |
|---|---|
| `random` | `random.randint()` picks a random index to choose a word and its matching hint |
| `list` | Stores words, hints, hangman drawings, guessed letters, wrong letters, and correct letters |
| `string` | `join()`, `in`, `count()`, `len()`, `upper()` build and check the word display |
| `while loop` | Keeps the round going until the player wins or makes 6 wrong guesses |
| `if-else` | Validates guesses and checks if a letter is correct, repeated, or invalid |
| `functions` | 5 functions — each handles one specific job |
| `input / output` | `input()` reads guesses; `print()` shows the game state every turn |

---

##How to Play

1. Run the program — a random word and a matching hint are chosen
2. The hint and word length are shown to help you get started
3. Guess one letter at a time
4. A correct guess reveals where that letter appears and how many times
5. A wrong guess adds a part to the hangman drawing
6. You have **6 wrong guesses** before the game ends
7. Guess the full word before the hangman is complete to win
8. Choose to play again after each round

---

## Demo

```
========================================
     HANGMAN — Word Guessing Game
========================================

  Hint   : Someone who writes code
  Length : 9 letters


    -----
    |   |
        |
        |
        |
    =====

  Word    : _  _  _  _  _  _  _  _  _
  Wrong   : 0 / 6
  Missed  : None
----------------------------------------
  Guess a letter : e

  'e' is in the word (2 time/s)!

  Word    : _  e  _  e  _  _  _  e  _
  Wrong   : 0 / 6
  Missed  : None
----------------------------------------
  Guess a letter : x

  'x' is not in the word. 5 left.

    -----
    |   |
    O   |
        |
        |
    =====
```

---

## How the Code Works

```
Program starts
      │
      ▼
choose_word()
  → picks a random index from the WORDS list
  → returns the word and its matching hint from HINTS
      │
      ▼
play() — one full round (while loop)
  │
  ├── show_word()
  │     → loops through the word string
  │     → builds a list: shows the letter if guessed, else "_"
  │     → joins the list into a spaced string for display
  │
  ├── get_guess()
  │     → keeps asking until input is exactly one valid, new letter
  │
  ├── if guess in word
  │     → word.count() shows how many times that letter appears
  │
  ├── is_won()
  │     → returns True only if every letter in the word has been guessed
  │
  └── HANGMAN[wrong]
        → uses the wrong-guess count as an index into the drawings list
```

---

## Project Structure

```
CodeAlpha_HangmanGame/
│
├── hangman.py         # Complete game — all code in one file
├── README.md          # Project documentation
├── requirements.txt   # Dependency info (none needed — built-in only)
└── .gitignore         # Excludes cache and OS files
```

---

## Functions Overview

| Function | What it does |
|---|---|
| `choose_word()` | Picks a random index and returns the matching word + hint |
| `show_word(word, guessed)` | Builds the display string — guessed letters shown, others hidden as `_` |
| `is_won(word, guessed)` | Returns `True` if every letter in the word has been guessed |
| `get_guess(guessed)` | Validates and returns a single new letter from the player |
| `play()` | Runs one full round — handles the game loop, win check, and loss message |

---

## Lists Used in This Project

| List | Purpose |
|---|---|
| `WORDS` | Stores the 5 possible words to guess |
| `HINTS` | Stores one hint per word, matched by index to `WORDS` |
| `HANGMAN` | Stores 7 ASCII drawings — one per stage, from 0 to 6 wrong guesses |
| `guessed` | Tracks every letter the player has tried during the round |
| `display` | Built inside `show_word()` — holds letters or blanks, then joined into a string |
| `wrong_list` | Filters `guessed` down to only the incorrect letters |
| `correct` | Filters `guessed` down to the correct letters, shown after a loss |

---

## Edge Cases Handled

- **Empty input** — asks the player to enter exactly one letter
- **Numbers or symbols** — rejected with a clear message
- **Repeated guesses** — detected and the player is asked to try a different letter
- **Replay** — the player can start a fresh round without restarting the program

---

## How to Run

```bash
# Make sure Python 3 is installed
python --version

# Run the game
python hangman.py
```

No installation needed — this project only uses Python's built-in `random` module.

---

## Author
SURAJ KUMAR SINGH

 
