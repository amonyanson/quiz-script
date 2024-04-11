def newgame():
	guesses = []
	correctguesses = 0
	questionsnum = 0
	for key in questions:
		print(key)
		for i in options:
			print(i)
		guess = input("Enter: [A, B, C or D]")
		guess = guess.upper()
		guesses.append(guess)
		correctguess += checkanswer(questions.get(key),guess)
		questionsnum += 1
	displayscore(correctguesses,guesses)
def checkanswer(answer, guess):
	if answer == guess:
		print("Correct")
		return 1
	else:
		print("Wrong")
		return 0
def displayscore(correctguesses, guesses): 
	print("Results") 
	print("Answer:") 
	for key in questions:
		print(questions.get(key),end=' ')
	print("Guesses:")
	for i in guesses:
		print(i, end=' ')
	score = int(correctguesses/4 * 100)
	print(f"You score is {score}%")
	print("YOu have successfully completed the test")
def playagain():
	response = input("Try again? [yes/no]:\n")
	response = response.lower()
	if response == "yes":
		return True
	elif response == "no":
		return False 

	else:
		print("You have placed the wrong input")
questions = {
"Who created python?": "A",
"In what year was python created?": "B",
"Python is tributed to which comedy group?": "C",
"Which is the greatest programming language of all time?": "D"
}

options = [
["A. Guido van rossum","B. Elon Musk","C. Jeff Bezos","D. Mark Zuckerburg"],
["A. 1990","B. 1991","C. 1992","D. 1993"],
["A. Cracked Python","B. Mr Robot","C. Monty Python","D. Pirates of the caribbean"],
["A. Javascript","B. Java","C. PHP","D. Python"]
]

newgame() 
while again():
	newgame()
