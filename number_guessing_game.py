number = 10
iterations = 0

while iterations < 3:
    user_guess = int(input("Guess: "))
    iterations += 1
    if user_guess == number:
        print("You guessed it!")
        break
else:
    print("Try again!")
