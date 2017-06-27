def QA(F):
	F(5,2)

def msg(A,B):
	print("hello my friend")
	QA(add)
	
def add(A,B):
	C = A+B
	print("%d + %d = %d" %(A,B,C))
	QA(timesTable)
	
def timesTable (A,B):
	print("Times table of %d" %A)
	for i in range(1,B+1):
		print(A,'x',i,'=',A*i)
		
QA(msg)		
		