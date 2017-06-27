class Results:
	
	def __init__(self,P=0,C=0,M=0):
		self.__phy = P
		self.__che = C
		self.__mat = M
		self.__ModulesFailed = 0
		
		
	def Physics(self,P):
		if(P >= 0 and P <= 150):
			self.__phy = P
						
			if (P < 70):
				print ("Failed Physics")
				self.__ModulesFailed += 1
							
		else:
			print("Invalid Physics mark")
			
	def Chemistry(self,C):
		if(C >= 0 and C <= 150):
			self.__che = C
			
			if (C < 70):
				print ("Failed Chemistry")
				self.__ModulesFailed += 1
			
		else:
			print("Invalid Chemistry mark")		
			
	def Maths(self,M):
		if(M >= 0 and M <= 150):
			self.__mat = M
			
			if (M < 70):
				print ("Failed Maths")
				self.__ModulesFailed += 1
		else:
			print("Invalid Maths mark")	
	
	def Calculations(self):
		self.Total=self.__phy+self.__che+self.__mat 
		self.Percent = self.Total * (100/450)
		
	def showResult (self):
		print(self.Total)
		print(self.Percent)
		
		if (self.__ModulesFailed == 1):
			print("Retake the exam")
			
		elif (self.__ModulesFailed == 2):
			print("Repeat the course")
			
		elif (self.__ModulesFailed == 3):
			print("You better go home Girl!!")
		
		
Peter = Results(0,0,0)
Peter.Physics(100)
Peter.Chemistry(5)
Peter.Maths(20)
Peter.Calculations()
Peter.showResult()
		
		
		