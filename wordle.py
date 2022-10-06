from random import choice
from colorama import Back, Style, Fore, init

# Resets my color/styles at the end of their respective lines
init(autoreset=True)

# Imports Mac built-in word list, filters to get only 5 letter words, then 'choice' chooses a random 5 letter word
word_list = [line.strip() for line in open("/usr/share/dict/words")]
filtered_list = choice(list(filter(lambda x: len(x) == 5, word_list)))

# Method to get the word from the user, checks to make sure it's a string and only 5 letters long, returns it as an uppercase word using '.upper'
def user_guess():
    while True:
        player_guess = input("Enter a 5 letter word! ")
        if type(player_guess) != str or len(player_guess) != 5:
            print("Invalid word, try again!")
            continue
        else:
            return player_guess.upper()


# -----START OF GAME-----will be brought here at file open and also at end of each game
play = True
while play == True:
    print()
    print(
        """
|-------------A Long Time Ago In a Terminal Far Far Away-------------------
| ____    __    ____  ______   .______       _______   __       _______   |
| \   \  /  \  /   / /  __  \  |   _  \     |       \ |  |     |   ____|  |
|  \   \/    \/   / |  |  |  | |  |_)  |    |  .--.  ||  |     |  |__     |
|   \            /  |  |  |  | |      /     |  |  |  ||  |     |   __|    |
|    \    /\    /   |  `--'  | |  |\  \----.|  '--'  ||  `----.|  |____   |
|     \__/  \__/     \______/  | _| `._____||_______/ |_______||_______|  |
|_________________________________________________________________________|
"""
    )
    print(
        Back.WHITE
        + Fore.BLUE
        + "   Hello there! Would you like to start a new game? Enter 'Yes' or 'Quit'  "
    )
    print()
    response = input().upper()
    print()
    if response == "QUIT":
        Play = False
        break
    elif response == "YES":
        print(Fore.BLUE + "Great! May the Force be with you.")
        print()

        # -----SET UP FOR MAIN LOOP-----
        guesses = 0
        output = [  # Create list to throw letters as strings into each index
            "",
            "",
            "",
            "",
            "",
        ]
        previous_guesses = []

        # -----MAIN LOOP-----
        while guesses < 6:
            print()
            print(
                "You have", 6 - guesses, "guesses left."
            )  # My guesses count up, so to show number of guesses remaining I had to subtract from 6
            guess = user_guess()  # Function defined above
            print()
            word = (
                filtered_list.upper()
            )  # Bring in my random word from above and set it to 'word'
            guess_list = list(guess)  # ex. ['G', 'U', 'E', 'S', 'S']
            random_word = list(
                word
            )  # ex. ['H', 'E', 'L', 'L', 'O'] split my words into a strings
            guesses = guesses + 1  # For each *valid* guess increase 'guesses' by 1
            for i in range(len(random_word)):  # Loops through every index of the list
                if (
                    guess_list[i] == random_word[i]
                ):  # If a letter of my guess word is in the correct spot of the word
                    output[i] = (
                        Fore.WHITE + Back.GREEN + guess_list[i] + Style.RESET_ALL
                    )
                elif (
                    guess_list[i] in random_word
                ):  # If a letter of my guess word is in the word but not correct spot
                    output[i] = (
                        Fore.WHITE + Back.YELLOW + guess_list[i] + Style.RESET_ALL
                    )
                else:  # If a letter of my guess word is not in the word at all
                    output[i] = Fore.WHITE + Back.RED + guess_list[i] + Style.RESET_ALL
            if guess_list == random_word:
                print(
                    Back.WHITE
                    + Fore.BLUE
                    + "The force is strong with you! The word was",
                    Fore.WHITE + Back.BLUE + "".join(output),
                )
            else:
                string_output = "".join(
                    output
                )  # Join the output back together into a string
                previous_guesses.append(
                    string_output
                )  # Add the output into previous guesses list
                print(
                    "\n".join(previous_guesses)
                )  # display output, drops each guess/output down a line so they are stacked
        print()
        random_word_string = "".join(random_word)  #
        print(
            Back.WHITE
            + Fore.BLUE
            + "Ouch! You lose! Try harder next time. The word was",
            Fore.WHITE + Back.BLUE + random_word_string,
        )
