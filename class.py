
class ONS:
	def message(self):
		print("hello my friend")
		self.add (7,2)
		
	def add(self,A,B):
		C = A + B
		print("Result: %d" %C)
		self.mult (7,3)

	#def mult(self,A,B):	
		#C = A * B 
		#print("Result: %d" %C)
		
	def mult(self,A=0,B=0,C=1):
		D=A+B+C
		print("Result: %d" %D)
		self.Add (3,2,5,4)
		
	def Add(self,*A):	
		C = 0
		for x in A:
			C = C + x
		print("Result: %d" %C) 	
		
		
Ref = ONS()
Ref.message()
