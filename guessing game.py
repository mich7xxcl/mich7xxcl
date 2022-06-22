import random

def guess(x):
    random_number= random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input (f'Guess the number between 1 and {x}: '))
        if guess<random_number:
            print ('Sorry, guess again, guess to low!')
        elif guess > random_number:
            print ('Sorry, guess again, guess to high!')

    print (f'\nYay, congrats you have guessed the {random_number} correctly!!!')
    print ('\nComputer\'s turn!\n')
    print('I\'m guessing between 1 and 100, so think of a number between that range!\n')
    print('Press (H) for guess too high, (L) guess too low, (C), guess correct\n')
       
guess(10)

    

def computer_turn (x):
    low = 1
    high = x
    feedback = ('')
    while feedback != 'c':
        if low != high:
            guess = random.randint (low, high)
        else:
            guess = low #could also be high because low=high
        feedback = input (f'Is {guess} too high (H), too low (L), correct (C)')
        if feedback == "h":
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'\nYay! The computer guessed {guess} correctly')


computer_turn(100)
