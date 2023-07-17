import random

numberofguesses = []
number = random.randrange(1, 100)

while True:
    
    guess = int(input("Please input a number between 1-100: "))
    
    
    if guess not in range(1, 101):
        print("Pick a number between 1-100 please.")
        continue

    if guess == number:
        numberofguesses.append(guess)
        again = input(f"Wow, you did it in {len(numberofguesses)} tries! Do you want to go again? (Y/N): ")
        if again == "Y":
            numberofguesses = [] 
            continue
        else:
            print("Hope you had fun!")
            break
    elif guess < number:
        print("Too low!")
        numberofguesses.append(guess)
        continue
    elif guess > number:
        print("Too high!")
        numberofguesses.append(guess)
        continue


    





  





