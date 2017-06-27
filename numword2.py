d = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
	6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
	11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
	15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
	19 : 'nineteen'}
d2 ={20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
	70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
d3 = 1000
	
def number(Number):
	if (Number >= 1) and (Number <19):
		return d[Number]

	if (Number >= 20) and (Number <90):
		if Number % 10 == 0: return d[Number]
		else:
		return d[Number // 10 * 10] + '-' + d[Number % 10]

	if (Number > d2) and (Number < 1000):
		if Number % 100 == 0: return d[Number // 100] + ' hundred'
		else: 
		return d[Number // 100] + ' hundred and ' + int_to_en(Number % 100)

	
	print("Your number is too large: %s" % str(Number))

