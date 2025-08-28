import random

secret_number = random.randint(1, 100)
guess = None
tries = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    tries +=1
    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        print(f"Correct! You got it! in {tries} tries")

