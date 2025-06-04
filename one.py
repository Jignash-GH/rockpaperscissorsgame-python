import random
my_list=['Rock', 'Paper', 'Scissors']
student = input("Choose Rock, Paper, or Scissors: ")

print("Your choice is: " + student)
computer= random.choice(my_list)
print("Computer's choice is: " + computer)
if student == computer:
    print("It's a tie!")   
elif student == 'Rock':
    if computer == 'Paper':
        print("You lose! Paper covers Rock.")
    else:
        print("You win! Rock crushes Scissors.")
elif student == 'Paper':
    if computer == 'Scissors':
        print("You lose! Scissors cut Paper.")
    else:
        print("You win! Paper covers Rock.")
elif student == 'Scissors':
    if computer == 'Rock':
        print("You lose! Rock crushes Scissors.")
    else:
        print("You win! Scissors cut Paper.")
else:
    print("Invalid choice! Please choose Rock, Paper, or Scissors.")
