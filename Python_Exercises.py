import sys, datetime, math, calendar
#from datetime import date
##Print multiline string
#print("""Twinkle, twinkle, little star,
#	How I wonder what you are! 
#		Up above the world so high,   		
#		Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
#	How I wonder what you are""")
##Print python version
#x = sys.version
#print()
#print(x)
##Print current date and time
#x = datetime.datetime.now()
#print()
#print(x)
##Calculate the area of a circle based on the radius input by the user
#x = math.pi * math.pow(int(input("Enter the circle's radius: ")),2)
#print()
#print(x)
##Show the user's name based on two inputs
#x = input("Enter ur first name: ")
#y = input("Enter ur family name: ")
#print()
#print("Ur name is " + x + " " + y)
##Make a list and a tuple based on user input
#x = input("Enter your list of numbers (separated by commas): ")
#y = x.split(",")
#z = tuple(y)
#print("The List:", y)
#print("The Tuple", z)
#print()
##Take a file name input and print its extention
#x = input("Input the full file name: ")
#y = x.split(".")
#print("The file's extentions is: " + y[-1])
##Display the first and last elements of a list
#x = ["Red","Green","White","Black"]
#print("The Colours are: ", x[0], x[-1])
##Display a date from a list
#x = (11, 12, 2014)
#print("The examination will be at {}.{}.{}".format(x[0], x[1], x[2]))
#print("The examination will be at: %i / %i / %i"%x)
##Accept the value n, an integer, and compute n^i
#x = int(input("Input ur number: "))
#def Exp(n, i):
#	if i > 3:
#		return 0
#	return math.pow(n, i) + Exp(n, i + 1)
#print(Exp(x, 1))
##Accept the value n, an integer, and compute n+nn+...+n[i]
#def Digit(n, i):
#	if i > 3:
#		return 0
#	y = 0
#	temp = i
#	while temp > 0:
#		y += n * math.pow(10, temp - 1)
#		temp -= 1
#	return y + Digit(n, i + 1)
#print(Digit(x, 1))
##Print a calander of a given month and year
#x = int(input("Input the month : "))
#y = int(input("Input the year : "))
#print(calendar.month(y, x))
##Calc difference between two days
#x1 = input("Enter your first date (separated by periods): ") #get the dates
#x2 = input("Enter your first date (separated by periods): ")
#y1 = x1.split(".") #turn them into lists of strings
#y2 = x2.split(".")
#y1 = [int(x) for x in y1] #one-line for to turn the lists of strings into list of ints
#y2 = [int(x) for x in y2]
#def DiffDates(d1, d2, m1, m2, y1, y2): #func to calc the date diff and display it
#	Dy = y2 - y1
#	Dm = m2 - m1
#	Dd = d2 - d1
#	print("The two days are " + str(Dy * 365.25 + Dm * 30.437 + Dd) + " days apart")
#	return
#DiffDates(y1[0], y2[0], y1[1], y2[1], y1[2], y2[2])
#y1 = date(y1[2], y1[1], y1[0])
#y2 = date(y2[2], y2[1], y2[0])
#print((y2 - y1).days)
##Print the volume of a sphere with a given radius
#x = int(input("Input the sphere's radius: "))
#print((4/3) * math.pi * math.pow(x,3))
#Get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
#def Eh17(n):
#	if n > 17:
#		return 2 * abs(n - 17)
#	return abs(n - 17)
#print(Eh17(22))
#Test whether a number is within 100 of 1000 or 2000
#def k1ork2(n):
#	if n > 900 and n < 1100 or n > 1900 and n < 2100:
#		print("Yes")
#	else:
#		print("No")
#k1ork2(192)