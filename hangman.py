import random

WORDS = ['python','jumble','football','game','computer', ]

#welcome the user
name = input('Enter your name: ')
print('Hello, ' + name, 'Lets play hangman')

print('So whats your first guess? ')

#here we set the word
word = random.choice(WORDS)

#creates veriable with empty value
guesses = ''

#set the number of turns
turns = 10

#creates while loop to check if the number of turns is zero
while turns > 0:

    #make counter that starts with zero
    failed = 0

    for char in word:

        #print charicter if in secret word
        if char in guesses:
            print(char)
        else:

            #if not found print dash
            print('_')

            #increse failed count by 1
            failed += 1
    #if failed equales zero print you won
    if failed ==0:
        print('You Won')

        #exit the script
        break
    print()
    
    #ask the user to guess a charicter
    guess = input('Guess a letter: ')

    #set player guess to guesses
    guesses += guess

    #if guess not found in word
    if guess not in word:

        #No of turns decresses by one
        turns -= 1
        print('Wrong Guess')

        #number of turns remainning
        print('You have', + turns, 'remainning')

        #if turns equals zero user lost
        if turns == 0:
            print('You Loose')
            print('The word was, ' + word)


