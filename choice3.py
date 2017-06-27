def menu():
	print ("your options are:")
	print ("" )
	print ("1 Addition")
	print ("2 Subtraction")
	print ("3 Division")
	print ("4 Multiplication")
	print ("5 Times Table")
	print ("6 QUIT")
	print (" ")
	return input ("Please choose your option: ")
 
 # this adds two numbers given
def add(a,b):
    print (a, "+", b, "=", a + b)
    
# this subtracts two numbers given
def sub(a,b):
    print (b, "-", a, "=", b - a)
    
# this divides two numbers given
def div(a,b):
	print (a, "/", b, "=", a / b)
# this multiplies two numbers given
def mul(a,b):
	print (a, "*", b, "=", a * b)

def ttb():
	A = int(input("Input your from number: "))
	B = int(input("Input your to number: "))  
	for i in range (1,B+1):
		print(A,'x',i,'=', A*i)

loop = 1
choice = 0
while loop == 1:
	choice = menu()
	if choice == "1":
		add (int(input("Insert 1st number: ")),int(input("Insert 2nd number: ")))
	elif choice == "2":
		sub (int(input("Subtract this: ")),int(input("from this: ")))
	elif choice == "3":
		div(int(input("Divide this: ")),int(input("by this: ")))
	elif choice == "4":
		mul (int(input("Multiply this: ")),int(input("by this: ")))
	elif choice == "5":
		ttb()
	elif choice == "6":
		loop = 0
	else:
		input("Invalid option selected, please try again...")
	input()
	
  
   