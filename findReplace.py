#This created the file "Hello my friend" and then appended to it
#msg = input()
#f = open("ABC.txt","a")
#f.write ("my name is Jane ")
#f.close()

with open("ABC.txt") as f:
	newText = f.read().replace('e','3')
	
with open("ABC.txt", "w") as f:
		f.write(newText)