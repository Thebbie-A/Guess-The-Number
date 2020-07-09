import random

# Generate random numbers between 0 and 20
for x in range(10):
  print(random.randint(0,20))

hide = random.randrange(0, 20)
print(hide)

#Guess a number by asking the user
guess = int(input("Enter your guess: "))
if guess > hide:
    print("Your guess is too high")
else:
    print("Your guess is too low")

# Write a programme where the computer randomly generates a number between 0 and 20.
# The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high,
# or too low. This will get you started with the random library if you haven't already used it.



