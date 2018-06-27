
# just making sure the user puts in a word
while True:
	word = input("Type a word for someone to guess: ")
	word = word.lower()
	if(word.isalpha() == False):
		print("That's not a word")
	else:
		break

guesses = [] #an emply list for the guesses
numfails = 0 #how many times the player has failed
maxfails = 7 #the max number of fails
wordToGuess = [] #the word that's going to be guessed. the underscores

# goes through the word, appends an underscore for every letter in the word to the list 'wordToGuess'
for letter in word:
	wordToGuess.append("_");

# this is the huge long time that separates the rounds of the game
for idx in range(0, 20):
	print(" ")

done = False
# not done is not False
while not done:
	print("-----------------------------------")
	print("Lives Left: ", maxfails - numfails) #max fails is 7 at the start
	print("Guesses So Far: ", guesses) # the empty list at the beginning
	print("Current Word: ", wordToGuess) #list of underscores

	guess = input("Guess a letter: ")
	guess = guess.lower() #hangman is not a case sensitive game!!

	if(len(guess) > 1): #can only guess one letter at a time
		print("That's too long!")
	elif(guess.isalpha() == False): #has to also be a letter!
		print("That's not a letter!")
	elif(guess in guesses): #can't be in the list of used guesses!
		print("You already guessed that!")
	else:
		guesses.append(guess) #if the guess is good to go add it to the list of guesses

		if(guess in word):  #checks if the guessed letter is in the word.
			print("You got a letter!")
			for idx in range(0, len(word)): #how it knows where to go into the wordToGuess. if the letter 'j' is the first letter, it needs to fill in wordToGuess at index 0
				if word[idx] == guess:
					wordToGuess[idx] = guess

			done = True #sets done to True
            # then it iterates through it again looking for underscore
            # if it sees an underscore it goes oh snap! i'm not done yet
            # sets done to false
			for idx in range(0, len(wordToGuess)):
				if wordToGuess[idx] == "_":
					done = False
					break
			if done: #if done user wins
				print("You won!")
		else: #if the guessed letter is not in the word
			print("Wrong guess!")
			numfails += 1 #num fails increments if the guess was wrong

			if numfails >= maxfails: #if numfails is higher or equal to maxfails the game ends and is lost
				print("You lost!")
				done = True
