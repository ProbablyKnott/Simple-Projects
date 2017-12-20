import random

def main():
	print("\nThis program generates a random number from 1 to 100 and allows you to guess what the number is.\nIt also tells you if you were higher or lower until you guess the right number or quit.\n")

	num = random.randrange(1,101)

	guess = input("What is the number? ")
	while guess != "quit" and guess != "QUIT" and int(guess) != num:
		if int(guess) > num:
			guess = input("The number you guessed was too high, guess again or type 'quit' to quit: ")
		elif int(guess) < num:
			guess = input("The number you guessed was too low, guess again or type 'quit' to quit: ")

	if int(guess) == num:
		print("You got it!")
	
main()