import random
print("I am thinking of a number between 1 and 100! ")
SecretNumber = random.randint(1, 100)
while True:
    Guess = int(input("Guess a number: "))
    if Guess == SecretNumber:
        print("Correct! Game Over. ")
        break
    elif Guess > SecretNumber:
        print("A little lower. ")
    elif Guess < SecretNumber:
        print("A little higher. ")
