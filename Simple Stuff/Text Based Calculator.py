'''
Written by: Michael Knott
Date: 12/14/2017
Github: https://github.com/ProbablyKnott/Simple-Stuff
Twitter: www.twitter.com/probablyknott
'''

class calc():

	def add(self, num1, num2):
		answer = num1 + num2
		return answer
	
	def subtract(self, num1, num2):
		answer = num1 - num2
		return answer
	
	def multiply(self, num1, num2):
		answer = num1*num2
		return answer
	
	def divide(self, num1, num2):
		answer = num1/num2
		return answer
	
	def remainder(self, num1, num2):
		answer = num1%num2
		return answer
		
	def power(self, num1, num2):
		answer = num1**num2
		return answer
		
	def root(self, num1, num2):
		power = 1/num2
		answer = num1**power
		return answer
	
	def clear(self):
		pass
		

#def main():
print("This program is a text based scientific calculator.\n")
	
widget = calc()
num1 = "Anything"
operator = "Anything"
num2 = "Anything"
	
while num1 != "QUIT" and num1 != "quit" and operator != "quit" and operator != "QUIT" and num2 != "quit" and num2 != "QUIT":
	
	num1 = input("Please enter a number or type 'quit' to quit: ")
	if num1 != "quit" and num1 != "QUIT":
		operator = input("Please enter an operator (+-*/%^r), type 'clear' to clear, or type 'quit' to quit: ")
		if operator != "quit" and operator != "QUIT":
			if operator == "clear" or operator == "CLEAR":
				widget.clear()
			else:
				num2 = input("Please enter another number so the function can be completed or clear/quit: ")
				if num2 != "quit" and num2 != "QUIT":
					if num2 != "clear" or operator != "CLEAR":
						print("Your function is: " + num1 + operator + num2)
			
					num1 = float(num1)
					num2 = float(num2)
			
					if num2 == "clear" or operator == "CLEAR":
						widget.clear()
					elif operator == "+":
						print(widget.add(num1, num2), "\n")
					elif operator == "-":
						print(widget.subtract(num1, num2), "\n")
					elif operator == "*":
						print(widget.multiply(num1, num2), "\n")
					elif operator == "/":
						print(widget.divide(num1, num2), "\n")
					elif operator == "%":
						print(widget.remainder(num1, num2), "\n")
					elif operator == "^":
						print(widget.power(num1, num2), "\n")
					elif operator == "r":
						print(widget.root(num1, num2), "\n")
			
	
	
