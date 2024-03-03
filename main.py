import random

still_playing = True
while still_playing:
    random_number = random.randint(1,100)

    difficulty_level = input("Which level of dificulty You choose? Type 'easy' or 'hard': ")

    if difficulty_level == "easy":
        attempts = 10
    else:
        attempts = 5
    still_guessing = True
    while still_guessing:
        guessed_number = int(input("Guess the number from 1 to 100: "))
        if guessed_number == random_number:
            print("You win! The number was correct")
            break
        elif guessed_number > random_number:
            print("too high!")
        elif guessed_number < random_number:
            print("too low!")
        attempts -= 1
        if attempts == 0:
            still_guessing = False
            print("You loose, maybe next time.")
        print(f"You have {attempts} attempts left")
    another_round = input("Another round maybe? Type 'y' or 'n': ")
    if another_round == "n":
        still_playing = False
