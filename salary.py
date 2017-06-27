Salary = input ("Please input Salary: ")
Grade = input ("Please specify the Grade: ")
Department = input ("Please  input Department (IT / HR) : ")
CTO = input ("Are you a CTO? (Y for yes or N for no) : ")

Salary = int(Salary)
Grade = int(Grade)
Department = int (Department)
Bonus=0
Tax=0
	
if Salary > 15000:
	if (Department == 1):
		if (CTO ==Y):
			SalaryAfterTax = Salary
		elif(Grade >= 1 and Grade <=10):
			Tax = Salary * 0.09
		elif (Grade >= 11 and Grade <=20):
			Tax = Salary * 0.15
		CalcBonus = SalaryAfterTax * 0.05
		Bonus = CalcBonus + SalaryAfterTax
	
	else:
		if (CTO == Y):
			Tax = Salary * 0.02
		
		elif(Grade >= 1 and Grade <=10):
			Tax = Salary * 0.09
						
		elif(Grade >= 11 and Grade <=20):
			Tax = Salary * 0.17
			
SalaryAfterTax = Salary - Tax
print ("Salary:%d" %Salary)	
print ("Tax:%f" %Tax)
print ("Salary After Tax - : %d" %(SalaryAfterTax))
print ("Salary with Added Bonus: %d" %(Bonus))