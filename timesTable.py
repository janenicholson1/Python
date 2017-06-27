num1 = int(input("Input your from number: "))
num2 = int(input("Input your to number: "))

step=1

if num1>num2:
	step=-1
	print ("\n Times table for: %d" %num1)
for T in range(num1,num2,step ): # 1st is starting, 2nd is ending 3rd is increment 
	for B in range(1,11):
		print("%dx%d=%d"%(T,B,(T*B)))
	
	#prompt user to decide whether d descending or other (ascending)  implement if statement to choose