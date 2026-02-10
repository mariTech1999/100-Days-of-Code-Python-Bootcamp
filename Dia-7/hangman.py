import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

placeholder = ["_"]*len(chosen_word)

ph = " ".join(placeholder)

lives = 6
print(hangman_art.stages[lives])
print(ph)

used_letters = []

while "_" in ph:
    print(f"Lives: {lives}")
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter")

    else:
        used_letters.append(guess)
        if guess in chosen_word:
            for pos, letter in enumerate(chosen_word):
                if letter == guess:
                    placeholder[pos] = guess

        else:
            print(f"Letter not in the word: {guess}")
            lives -= 1
        print(hangman_art.stages[lives])
        ph = " ".join(placeholder)
        print(ph)

        if lives == 0 :
            print("You Lose! The word was " + chosen_word)
            exit()

print("Congratulations! You guessed the word!")