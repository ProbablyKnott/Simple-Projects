from tkinter import *

'''
Written by: Michael Knott
Date: 12/22/2017
Github: https://github.com/ProbablyKnott/Simple-Stuff
Twitter: www.twitter.com/probablyknott
'''

whichNum = None

#TODO:
#add squared, root, ! and 1/x button and change name of current root button to squareRoot
#add positive/negative button
#add unit conversion buttons
#add regular to scientific button
#make each frame a class and make a main tk window class 
#Find bug that makes functions give wrong value after multiple functions in a row

def button(buttonNum, whichNum):
	count = 0
	number = ""
	try:
		if whichNum == False and len(num1) == 0:
			num1.append(buttonNum)
			while count < len(num1):
				number = number + str(num1[count])
				count += 1
			screen["text"] = number
		elif whichNum == True and len(num2) == 0:
			num2.append(buttonNum)
			while count < len(num2):
				number = number + str(num2[count])
				count += 1
			screen["text"] = number
		elif whichNum == False and num1[0] != "0" and num1[0] == ".":
			num1.append(buttonNum)
			while count < len(num1):
				number = number + str(num1[count])
				count += 1
			screen["text"] = "0" + number
		elif whichNum == False and num1[0] != "0":
			num1.append(buttonNum)
			while count < len(num1):
				number = number + str(num1[count])
				count += 1
			screen["text"] = number
		elif whichNum == True and num2[0] != "0" and num2[0] == ".":
			num2.append(buttonNum)
			while count < len(num2):
				number = number + str(num2[count])
				count += 1
			screen["text"] = "0" + number
		elif whichNum == True and num2[0] != "0":
			num2.append(buttonNum)
			while count < len(num2):
				number = number + str(num2[count])
				count += 1
			screen["text"] = number
	except:
		if whichNum == False:
			num1[0] = "."
		else:
			num2[0] = "."
		number = "0."
		screen["text"] = number
	
def buttonZero(whichNum):
	count = 0
	number = ""
	if whichNum == False:
		num1.append("0")
		while count < len(num1):
			number = number + str(num1[count])
			count += 1
	else:
		num2.append("0")
		while count < len(num2):
			number = number + str(num2[count])
			count += 1
	screen["text"] = number
	
def buttonDecimal(whichNum):
	count = 0
	number = ""
	if whichNum == False and "." not in num1:
		if len(num1) > 0:
			if num1[0] == "0":
				num1[0] = "."
				number = "0."
			else:
				num1.append(".")
				while count < len(num1):
					number = number + str(num1[count])
					count += 1
		else:
			num1.append(".")
			number = "0" + num1[0]
	elif whichNum == False:
		while count < len(num1):
				number = number + str(num1[count])
				count += 1
		number = "0" + number
	elif whichNum == True and "." not in num2:
		if len(num2) > 0:
			if num2[0] == "0":
					num2[0] = "."
			else:
				num2.append(".")
				while count < len(num2):
					number = number + str(num2[count])
					count += 1
		else:
			num2.append(".")
			number = "0" + num2[0]
	elif whichNum == True:
		while count < len(num2):
			number = number + str(num2[count])
			count += 1
		number = "0" + number
	screen["text"] = number

def commandButtonPress(symbol):
	global whichNum
	if whichNum == False:
		if len(operator) > 0 and operator[0] == "+":
			operator.remove("+")
		if len(operator) > 0 and operator[0] == "-":
			operator.remove("-")
		if len(operator) > 0 and operator[0] == "*":
			operator.remove("*")
		if len(operator) > 0 and operator[0] == "/":
			operator.remove("/")
		if len(operator) > 0 and operator[0] == "^":
			operator.remove("^")
	if len(num1) > 0:
		operator.append(symbol)
		screen["text"] = operator[0]
		whichNum = True

def equals():
	global whichNum
	if operator[0] == "+":
		answer = add()
		whichNum = False
	if operator[0] == "-":
		answer = subtract()
		whichNum = False
	if operator[0] == "*":
		answer = multiply()
		whichNum = False
	if operator[0] == "/":
		answer = divide()
		whichNum = False
	if operator[0] == "^":
		answer = power()
		whichNum = False
	screen["text"] = answer
	count = len(num1)-1
	while count >= 0:
		num1.remove(num1[count])
		count -= 1
	count = 0
	answerStr = str(answer)
	while count < len(answerStr):
		num1.append(answerStr[count])
		count += 1
	#print(num1)
	count = len(num2)-1
	while count >= 0:
		num2.remove(num2[count])
		count-=1

def add():
	if len(num2) > 0:
		number1 = ""
		number2 = ""
		count = 0
		while count < len(num1):
			number1 += num1[count]
			count+=1
		count = 0
		while count < len(num2):
			number2 += num2[count]
			count+=1
		answer = float(number1) + float(number2)
		return answer
	
def subtract():
	if len(num2) > 0:
		number1 = ""
		number2 = ""
		count = 0
		while count < len(num1):
			number1 += num1[count]
			count+=1
		count = 0
		while count < len(num2):
			number2 += num2[count]
			count+=1
		answer = float(number1) - float(number2)
		return answer

def multiply():
	if len(num2) > 0:
		number1 = ""
		number2 = ""
		count = 0
		while count < len(num1):
			number1 += num1[count]
			count+=1
		count = 0
		while count < len(num2):
			number2 += num2[count]
			count+=1
		answer = float(number1) * float(number2)
		return answer

def divide():
	if len(num2) > 0:
		number1 = ""
		number2 = ""
		count = 0
		while count < len(num1):
			number1 += num1[count]
			count+=1
		count = 0
		while count < len(num2):
			number2 += num2[count]
			count+=1
		answer = float(number1) / float(number2)
		return answer

def power():
	if len(num2) > 0:
		number1 = ""
		number2 = ""
		count = 0
		while count < len(num1):
			number1 += num1[count]
			count+=1
		count = 0
		while count < len(num2):
			number2 += num2[count]
			count+=1
		answer = float(number1) ** float(number2)
		return answer
		
def root(whichNum, num1, power):
	if whichNum == False:
		count = 0
		number = ""
		while count < len(num1):
			number += num1[count]
			count += 1
		answer = float(number) ** (1/power)
		screen["text"] = answer
		num1 = str(answer)
	
def clear(num1, num2):
	global whichNum
	count = len(num1)-1

	while count >= 0:
		num1.remove(num1[count])
		count-=1
	count = len(num2)-1
	while count >= 0:
		num2.remove(num2[count])
		count-=1
	screen["text"] = "0"
	whichNum = False
	
def main():
	window = Tk()
	window.title("Calculator")
	window.geometry("250x305")
	global num1
	num1 = []
	global num2
	num2 = []
	global operator
	operator = []
	global whichNum
	whichNum = False
	
	frame1 = Frame(height = 25, width = 220)
	frame1.pack(expand=False)
	global screen
	screen = Label(frame1, text="0", height = 5, width = 30)
	screen.pack(side = LEFT, expand=False, anchor = N, padx=[5, 5])

	frame2 = Frame(height = 225, width = 220)
	frame2.pack(anchor = S)
	button1 = Button(frame2, text="1", command = lambda: button("1", whichNum))
	button1.grid(column=0, row=2)
	button2 = Button(frame2, text="2", command = lambda: button("2", whichNum))
	button2.grid(column=1, row=2)
	button3 = Button(frame2, text="3", command = lambda: button("3", whichNum))
	button3.grid(column=2, row=2)
	button4 = Button(frame2, text="4", command = lambda: button("4", whichNum))
	button4.grid(column=0, row=3)
	button5 = Button(frame2, text="5", command = lambda: button("5", whichNum))
	button5.grid(column=1, row=3)
	button6 = Button(frame2, text="6", command = lambda: button("6", whichNum))
	button6.grid(column=2, row=3)
	button7 = Button(frame2, text="7", command = lambda: button("7", whichNum))
	button7.grid(column=0, row=4)
	button8 = Button(frame2, text="8", command = lambda: button("8", whichNum))
	button8.grid(column=1, row=4)
	button9 = Button(frame2, text="9", command = lambda: button("9", whichNum))
	button9.grid(column=2, row=4)
	button10 = Button(frame2, text="0", command = lambda: buttonZero(whichNum))
	button10.grid(column=1, row=5)

	button11 = Button(frame2, text="+", command = lambda: commandButtonPress("+"))
	button11.grid(column=3, row=2)
	button12 = Button(frame2, text="-", command = lambda: commandButtonPress("-"))
	button12.grid(column=3, row=3)
	button13 = Button(frame2, text="*", command = lambda: commandButtonPress("*"))
	button13.grid(column=3, row=4)
	button14 = Button(frame2, text="/", command = lambda: commandButtonPress("/"))
	button14.grid(column=3, row=5)
	button15 = Button(frame2, text="^", command = lambda: commandButtonPress("^"))
	button15.grid(column=0, row=1)
	button16 = Button(frame2, text="sqr", command = lambda: root(whichNum, num1, 2))
	button16.grid(column=1, row=1)
	button17 = Button(frame2, text=".", command = lambda: buttonDecimal(whichNum))
	button17.grid(column=0, row=5)
	button18 = Button(frame2, text="=", command = lambda: equals())
	button18.grid(column=2, row=5)
	button19 = Button(frame2, text="C", command = lambda: clear(num1, num2))
	button19.grid(column=3, row=1)
	window.mainloop()

main()
