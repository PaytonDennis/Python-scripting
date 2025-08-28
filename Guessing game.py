from enum import nonmember

secret_number = 37

guess = None

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        print("Correct!")



