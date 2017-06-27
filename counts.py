chars = "abcdefghijklmnopqrstuvwxyz"

strinput = input("Please input your sentence: ")
d = {}
for A in strinput:
	try:
		d[A] += 1
	except:
		d[A] = 1

for B in d.keys():
	print("%s:%d"%(B,d[B]))
