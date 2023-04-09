"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 1.8: Guessing Game
import random

name = input("Username: ")
print("Are you ready to start?")
answer = input("Type 'Yes' or 'No'!\n")
if answer == 'No':
    exit()
else:
    def main():
        # Generate the random number
        random_number = random.randint(1, 100)
        print("Guess the number generated randomly from 1 to 100!")
        attempts = 0
        # User guessed correctly
        while True:
            user_guess = int(input("Enter your answer: "))
            if user_guess == random_number:
                print('Congratulations! Your answer is completely correct in', (attempts + 1), 'attempts\n')
                # Asking for playing again
                choice = input("Do you want to play again? Type Yes or Exit!\n")
                if choice == 'Yes':
                    # generate randomly another number
                    random_number = random.randint(1, 100)
                    attempts = 0
                    continue
                else:
                    break
            # User guessed incorrectly and check if it is lower or higher    
            elif user_guess < random_number:
                print("It is lower than the correct answer, please try again!")
            else:
                print("It is higher than the correct answer, please try again!")
            attempts += 1
    main()
    