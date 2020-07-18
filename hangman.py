# HANGMAN
import random

# List of words to choose from

word_list = [
    'Quick',
    'Electric',
    'uphill',
    'Difficult',
    'Boruto',
    'Serverless',
    'Streamline',
    'Spaghetti'
]

# print(word_list)

# function to select a random word from word_list
def select_word():
    selected_word = random.choice(word_list)
    return selected_word.lower()


def get_started(selected):
    # print(selected)
    selected_dashes = "_" * len(selected)
    attempts = len(selected)
    guessed_letters = []
    complete = False
    player_name = input("Please, enter your playername! \n")
    print("Welcome, {} , Let's play Hangman. I hope you lose! :)".format(player_name))

    while not complete and attempts > 0:
        attempt = input("Guess a letter of the word! \n")
        if len(attempt) == 1 and attempt.isalpha():
        
            if attempt in guessed_letters: #check if attempt is in selected word
                print("You already guessed this letter ", attempt)
            elif attempt not in selected: #check if attempt is not in selected word
                attempts = attempts - 1  #decrease attempt counter
                print("Loser, letter {} is not in {}".format(attempt,selected_dashes))
                guessed_letters.append(attempt)   #add attempt to guessed letters list
            else:
                attempts = attempts - 1
                print("Nice, letter {} is in word {}".format(attempt,selected_dashes))
                guessed_letters.append(attempt)

                # print("".join(guessed_letters))
                dashes_list =  list(selected_dashes) #convert dashes representing each letter of word to list
                indexed_word = [ i for i,letter in enumerate(selected) if letter == attempt] #index letters of selected word 

                for index in indexed_word: #replace each dash with letter if correct
                    dashes_list[index] = attempt

                print(dashes_list)
                selected_dashes = ''.join(dashes_list)
                # print("DASH LIST")
                # print(''.join(dashes_list))
                if "_" not in "".join(dashes_list):
                    complete = True
        elif not attempt.isalpha() or len(attempt) > 1 :
            print("Ooops!, attempt is not an alphabet and may be greater than one", attempt)
        else:
            print("Oops! Invaid attempt")

    if complete:
        print("Great, you guessed {} correctly".format(selected))
    else:
        print("too bad, a man just got hanged!")
    




def main():
    selected_word = select_word()
    get_started(selected_word)


if __name__ == "__main__":
    main()