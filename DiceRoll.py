import random

def main():
	print("\nThis program outputs a random dice roll.\n")

	print (random.randrange(1,7), "\n")

	answer = input("Would you like to roll again? Type 'YES' to continue: ")
	while answer == "YES" or answer == "yes":
		print("\n")
		print (random.randrange(1,7),  "\n")
		answer = input("Would you like to roll again? Type 'YES' to continue: ")
	
main()