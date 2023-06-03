import random
import math


lower = int(input("Enter a lower limit:"))
upper = int(input("Enter an upper limit:"))

x = random.randint(lower,upper)
chances = round(math.log(upper - lower +1, 2))
print(f'You have got {chances} changes to guess the number')

count = 0

while count < chances:
    count = count + 1
    guess = int(input("Enter a number to guess:"))
    if x == guess:
        print(f'Congrats you have found it in {count} try')
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("You guess too big")
if count >= chances and x != guess:
    print(f'The number is {x}' '\n Better luck next time')

