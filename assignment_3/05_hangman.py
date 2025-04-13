# Hangman
# Give limited tries to the user to basically guess the word correctly before
# the hanged man is completely drawn

from hangman_visual import lives_visual_dict
from words import words
from random import choice

def main():
    retries : int = 7
    word : str = choice(words).lower()
    user_word : str = "_" * len(word)
    user_win : bool = False
    while retries > -1:
        # Render the image
        print("Hangman state:")
        print(lives_visual_dict[retries])
        print(f"Word : {user_word}")
        if retries == 0:
            break

        # If the user has completed the word, then game win!
        if user_word == word:
            user_win = True
            break

        # Take letter from user
        user_letter = input("Guess a letter: ").lower()[0]

        # Deduct retry if letter incorrectly guessed
        # Case 1: letter not in word at all
        if user_letter not in word:
            retries -= 1
            continue
        # Case 2: letter in word, but has been already guessed as many times as
        # present in the word
        elif word.count(user_letter) == user_word.count(user_letter):
            retries -= 1
            continue
        else:
            pass

        # Fill the correct letter once in the user_word
        new_user_word = ""
        letter_filled_once : bool = False
        for index in range(len(word)):
            # Skip if already present
            if user_word[index] == user_letter:
                new_user_word += user_letter
                continue
            # Write guessed letter if not already filled once and matches the
            # position in the word 
            if word[index] == user_letter and not letter_filled_once:
                letter_filled_once = True
                new_user_word += user_letter
                continue

            new_user_word += user_word[index]
        user_word = new_user_word
    
    # Tell if user won or lost
    if user_win:
        print("Yay, congrats! You won!")
    else:
        print("Oh no, you lost!")


if __name__ == '__main__':
    main()