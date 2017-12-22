#File: fibonacci.py
#Author: Michael Knott
#Date: 3/27/2017
#Prints the fibonacci sequence for a given number of iterations

def fibSeq(maxIterations):
    count = 1
    fibOld = 0
    fibNew = 1
    #print(fibNew)
    while count <= maxIterations:
        fibNew += fibOld
        fibOld = fibNew - fibOld
        print(count, ":", fibOld)
        #print(fibNew)
        count+=1

def main():
    userNum = int(input("How many values of the fibonacci sequence would you like to see?: "))
    fibSeq(userNum)
main()
