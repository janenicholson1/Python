class ONE:
	def __init__(self,A=0,B=0,C=0):
		self.A = A
		self.B = B
		self.C = C
		
	def __add__(self,R):
		C=ONE(0,0,0)
		C.A = self.A+R.A
		C.B = self.B+R.B
		C.C = self.C+R.C
		return C
		
	def __mul__(self,R):
		C=ONE(0,0,0)
		C.A = self.A*R.A
		C.B = self.B*R.B
		C.C = self.C*R.C
		return C
		
		
	def __sub__(self,R):
		C=ONE(0,0,0)
		C.A = self.A-R.A
		C.B = self.B-R.B
		C.C = self.C-R.C
		return C
		
	def __truediv__(self,R):
		C=ONE(0,0,0)
		C.A = self.A/R.A
		C.B = self.B/R.B
		C.C = self.C/R.C
		return C
		
	def __or__(self,R):
		C=ONE(0,0,0)
		C.A = self.A|R.A
		C.B = self.B|R.B
		C.C = self.C|R.C
		return C
	
A=ONE(100,2,303)
B=ONE(10,25,36)
C=A+B
X=A*B
Y=A-B
Z=A/B
T=A|B

print()
print ("Addition")
print(C.A) 
print(C.B)
print(C.C)
print()

print()
print ("Multiplication")
print(X.A)
print(X.B)
print(X.C)
print()

print()
print ("Subtraction")
print(Y.A)
print(Y.B)
print(Y.C)
print()

print()
print ("Division")
print(Z.A)
print(Z.B)
print(Z.C)

print()
print ("Or")
print(T.A)
print(T.B)
print(T.C)