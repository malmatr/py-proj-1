import random
import hangman_art
import hangman_words

stages = hangman_art.stages
word_list = hangman_words.word_list
hidden_word = random.choice(word_list)
complete = False
lives = 6

print(hangman_art.logo)

display = []
for d in range(len(hidden_word)):
    display.append("_")

while not complete:
    user_guess = input("Guess a letter:\n").lower()

    if user_guess in display:
        print(f"You've already guessed {user_guess}")

    for position in range(len(hidden_word)):
        letter = hidden_word[position]
        if letter == user_guess:
            display[position] =letter

    if user_guess not in hidden_word:
        lives -= 1
        if lives == 0:
            complete = True
            print(f"You lose! The correct answer is {hidden_word}")
        
    print(f"{' '.join(display)}")


    if "_" not in display:
        complete = True
        print("You win!")
    print(hangman_art.stages[lives])

