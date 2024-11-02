import random

#Get a number for the range maximum from user and verify int
top_num = input('Type a number: ')

if top_num.isdigit():
    top_num = int(top_num)

    if top_num <= 0:
        print('Please type a number larger than 0')
        quit()

else:
    print('That was not a number. Goodbye!')
    quit()

#Pick a random number and initialize guess count
random_number = random.randint(0, top_num)
guesses = 0

#User guess loop
while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please guess a number next time.')
        continue

    if user_guess == random_number:
        print('You got it right!')
        break
    elif user_guess > random_number:
        print('That number is too high.')
    else:
        print('That number is too low.')


#Provide guess count
print('You guessed the number in',guesses, 'guesses.')




