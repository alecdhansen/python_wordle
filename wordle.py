from random import choice
from colorama import Back, Style, Fore, init

init(autoreset=True)

# Imports Mac built-in word list, filters to get all 5 letter words, then 'choice' chooses a random 5 letter word
# wordlist = [line.strip() for line in open("/usr/share/dict/words")]
# filteredList = choice(list(filter(lambda x: len(x) == 5, wordlist)))
# print(filteredList)

word_list = ["hello", "react"]
word = choice(word_list)
print(Fore.CYAN + word)
# print(len(word))
play = True
while play == True:
    print()
    print(
        Back.WHITE
        + Fore.BLUE
        + "Would you like to start a new game? Enter 'Yes' or 'Quit'"
    )
    print()
    response = input().lower()
    print()
    if response == "quit":
        Play = False
    elif response == "yes":
        guesses = 0
        print("Great! Let's play WORDLE! Enter a 5 letter word: ")
        while guesses < 6:
            guess = input().lower
            guesses = guesses + 1
            output = ""
            for i in range(len(word)):
                if guess[i] == word[i]:
                    output = output + guess[i]
                elif guess[i] in word:
                    output = output + guess[i]
                else:
                    guess = output + guess[i]
            print(guess)
            if guess == word:
                print("You guessed it! The word was", word)
                guess = guesses + 6
            guesses = guess + 1
