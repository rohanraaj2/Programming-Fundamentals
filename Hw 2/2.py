secret_number = int(input())
def guessing_game(secret_number, num_tries):
    for i in range (1, 6):
        x = int(input())
        print ("Attempt number", i)
        if i == 5 and x != secret_number:
            print("Sorry, you lose! Too many wrong guesses.")
        else:
            if x < secret_number:
                print("Try again! Your guess is too low.")
            elif x > secret_number:
                print("Try again! Your guess is too high.")
            elif x == secret_number:
                print("Congratulations, you won! You guessed the secret number", secret_number, "in", i, "guesses.")
                break
    
guessing_game(secret_number, 1)
