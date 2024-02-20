import random                                                                           #import random module
secretNumber = random.randint(1, 20)                                                    #secret number will be a random integer (randint) value between 1-50
print('I am thinking of a number between 1 and 50.')                                    #print statement

for guessesTaken in range(1, 6):                                                        #ask the playter to guess 5x range(1, 6) #guessesTaken is an integer value tracking number of attempts
    print('Take a guess')                                                               #print statement
    guess = int(input())                                                                #translate the string input into an integer for math processing 
    if guess < secretNumber:                                                            #compare guess to secretnumber and the return to beginning of the for loop
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Guess too high')
    else:                                                                               #guess not too high or too low so break out of this for loop and move on to next argument
        break

if guess == secretNumber:                                                               #if you guessed corretly in 5x tries give congrats response otherwise run else code block
    print('Congrats! You guessed my number in ' + str(guessesTaken) + ' tries.')        #convert the integer guessesTaken to a string value in order to print it
else:
    print('Nope. The number I was thinking of was: ' + str(secretNumber))               #convert integer secretNumber to str() in order to print it as text
