#Task 8

secret_phrase = open('secret_phrase.txt', 'r')
shown_phrase = secret_phrase.read()[:-1]

guessed = []
wrong = []
tries = 10
count = 0

while tries > 0:
    out = ""
    for letter in shown_phrase:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"
    count += 1


    if out == shown_phrase :
        print "You guessed", shown_phrase
        break

    print "Guess the word:", out

    guess = raw_input()

    if guess in guessed or guess in wrong:
        print "Already guessed", guess
    elif guess in shown_phrase:
        print "Yay"
        guessed.append(guess)
    else:
        print "Nope"
        tries = tries - 1
        wrong.append(guess)
        #print ()

if tries:
    print "You guessed", shown_phrase
else:
    print "You didn't get", shown_phrase



#We created the file secret_phrase.txt that contained on a single line and all in lowercase letters the word the wanted people to guess.
#We used the f.read() function to read the file data and store it in a variable shown_phrase.
#We use a for loop to build up some text with an underscore for each letter in the word.
#The word strawberry put in, will write out as many underscores as the letters that composed the word, to the screen.
#We use the  function raw.input to find out what the player typed. We use if to find out if the letter was in the word.
#What we have done is put a loop, like forever in scratch, that will keep asking for letters from the player, until they guess the word.
#We also use a list, guessed, which we add the letters to when they are right.
#This program will loop forever until all the letters are guessed.
#We are using a new list, wrong, to store all the guesses that were not right.

#Edge cases
#1. Once a letter is guessed correctly, it is no more displayed after another letter is guessed. For this reason, we suggest to type the letters in the guessed brakets, one after the other, without deleting any.
#2. The printing statements are apparently not working, thus the count of the attempts too
