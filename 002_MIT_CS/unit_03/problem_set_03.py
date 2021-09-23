# We are going to make hangman

# Implement a function, called hangman

# Use provided files.

# 1. The computer selects a random word from a list of words.

# 2. The game is interactice the flow is:
#    a. The user is told how many letters the word has.
#    b. The user supplies a letter.
#    c. The computer checks if the letter is in the word. and gives the user feedback.
#    d. The user is shown the partially guessed word, and the letters they have not guessed.

# 3. The user has 8 guesses.
# if the user runs out of guesses the games is over and the word is revealed.

# Examples game:

	# Loading word list from file...
	# 55900 words loaded.
	# Welcome to the game Hangman!
	# I am thinking of a word that is 4 letters long
	# -----------
	# You have 8 guesses left
	# Available Letters: abcdefghijklmnopqrstuvwxyz
	# Please guess a letter: a
	# Oops! That letter is not in my word: _ _ _ _
	# -----------
	# You have 7 guesses left
	# Available Letters: bcdefghijklmnopqrstuvwxyz
	# Please guess a letter: b
	# Oops! That letter is not in my word: _ _ _ _
	# -----------
	# You have 6 guesses left
	# Available Letters: cdefghijklmnopqrstuvwxyz
	# Please guess a letter: c
	# Oops! That letter is not in my word: _ _ _ _
	# -----------
	# You have 5 guesses left
	# Available Letters: defghijklmnopqrstuvwxyz
	# Please guess a letter: d
	# Oops! That letter is not in my word: _ _ _ _
	# -----------
	# You have 4 guesses left
	# Available Letters: efghijklmnopqrstuvwxyz
	# Please guess a letter: e
	# Good guess: e_ _ e
	# -----------
	# You have 4 guesses left
	# Available Letters: fghijklmnopqrstuvwxyz
	# Please guess a letter: f
	# Oops! That letter is not in my word: e_ _ e
	# -----------
	# You have 3 guesses left
	# Available Letters: ghijklmnopqrstuvwxyz
	# Please guess a letter: g
	# Oops! That letter is not in my word: e_ _ e
	# -----------
	# You have 2 guesses left
	# Available Letters: hijklmnopqrstuvwxyz
	# Please guess a letter: h
	# Oops! That letter is not in my word: e_ _ e
	# -----------
	# You have 1 guesses left
	# Available Letters: ijklmnopqrstuvwxyz
	# Please guess a letter: i
	# Oops! That letter is not in my word: e_ _ e
	# -----------
	# Sorry, you ran out of guesses. The word was else. 