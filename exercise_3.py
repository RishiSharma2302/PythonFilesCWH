# guessing game

chances = 5  # no of chances
answer = 34  # correct answer

print("WELCOME TO THE GUESSING GAME! YOU HAVE 5 CHANCES TO GUESS THE RIGHT NUMBER :)")

while chances:
    print("\nWhat's your guess? (You have", chances, "lives left)", end=": ")
    guess=int(input())

    if guess == answer:
        print("Congratulations! You have guessed the right number in", 6-chances, "guesses")
        break
    elif abs(answer - guess) < 10:
        chances = chances - 1
        print("you are close")
        if guess > answer:
            print("Try a little smaller number", end=". ")
        else:
            print("Try a little larger number", end=". ")

    else:
        chances = chances - 1
        print("You are very much out of range!", end=" ")
        if guess>answer:
            print("Try a smaller number", end=". ")
        else:
            print("Try a larger number", end=". ")

if chances == 0:
    print("You lost!!")
else:
    print("Thank you for playing!")
