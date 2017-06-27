#num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
#			6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
#			11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
#			15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
#num2words2 = [20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70:'Seventy', 'Eighty', 'Ninety']

def number(Number):
	d = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
		6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
		11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
		15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
		19 : 'nineteen', 20 : 'twenty',
		30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
		70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
	k = 1000
	m = k * 1000

	assert(0 <= num)

	if (num < 20):
		return d[num]

	if (num < 100):
		if num % 10 == 0: return d[num]
		else: return d[num // 10 * 10] + '-' + d[num % 10]

	if (num < k):
		if num % 100 == 0: return d[num // 100] + ' hundred'
		else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

	if (num < m):
		if num % k == 0: return int_to_en(num // k) + ' thousand'
		else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

	if (Number >= 1) and (Number <= 19):
		return num2words1[Number]
	elif (Number >= 20) and (Number < 99):
		##tens, below_ten = divmod(Number, 10)
		return (num2words2[tens - 2]) + '-' + (num2words1[below_ten])
		
	else:
		print("Number Out Of Range")
		main()
	print(Number)
def main():
	num = eval(input("Please enter a number between 0 and 99: "))
	number(num)
main()


