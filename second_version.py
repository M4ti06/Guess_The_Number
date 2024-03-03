import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high!")
        return turns - 1
    elif guess < answer:
        print("too low!")
        return turns - 1
    else:
        print(f"You got it. The answer is {answer}")


def set_difficulty():
    level = input("Choose the difficulty. Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of the number between 1 and 100.")
    answer = random.randint(1,100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You run out of attempts, You loose")
            return

game()