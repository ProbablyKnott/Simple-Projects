import random

print("This program is an addition game. Pick the right answer to the equation.\n")

userInput = "nothing"

while userInput != "quit" and userInput != "QUIT":
	num1 = random.randrange(1,11)
	num2 = random.randrange(1,11)
	answer = num1 + num2

	fake1 = random.randrange(1,22)
	fake2 = random.randrange(1,22)
	while fake1 == fake2:
		fake2 = random.randrange(1,22)
	
	answerList = [fake1, fake2, answer]
	random.shuffle(answerList)
	
	correct = False
	while correct == False and userInput != "quit" and userInput != "QUIT":
		print("\t" + str(num1) + " + " + str(num2) + " = ?\n")
		print("\tA   B   C")
		print("\t" + str(answerList[0]) + "   " + str(answerList[1]) + "   " + str(answerList[2]))
	
		userInput = input("\nPlease type the number or corresponding letter of the answer or 'quit' to quit: ")
	
		answersPossible = ["A","B","C"]
		count = 0
		userSpot = 0
		while count < 3:
			if userInput == answersPossible[count]:
				userSpot = count
			count+=1
	
		if userInput == str(answer) or answerList[userSpot] == answer:
			correct = True
			print("\n\tYou Got It!\n")
		elif userInput != "QUIT" and userInput != "quit":
			print("\n\tTry again!\n")