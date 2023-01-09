import random

# rand1 = random.randrange(-5,11)  # doesn't includes the upper bound 11 number

# print(rand1)

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0")
        quit()
        
else:
    print("Please enter a digit")
    quit()


random_number = random.randint(0,top_of_range)    # includes the upper bound 11 number 

# print(random_number)

guess = 0

while True:
    guess = guess + 1
    user_guess = input("Guess the number: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Make sure you entered a number")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")    

print("\n")
print(f"You got it in {guess} guesses...") 













