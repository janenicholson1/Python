import os

inputFilename = 'plain.txt'
outputFilename = 'plain.encrypted.txt'
myKey = 5
myMode = 'encrypt'

if not os.path.exists(inputFilename):
	print('The file %s does not exist. Quitting...' % (inputFilename))
	sys.exit()
	
if os.path.exists(outputFilename):
	print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
	response = input('> ')
	if not response.lower().startswith('c'):
		sys.exit()
	

fileObj = open(inputFilename)
content = fileObj.read()
encrypted = ""
for letter in (content):
	if letter == " ":
		encrypted += " "

	else: 
		encrypted += chr(ord(letter) + 5)
fileObj.close()

print('%sing...' % (myMode.title()))


outputFileObj = open(outputFilename, 'w')
outputFileObj.write(encrypted)
outputFileObj.close()
print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
#print('%sed file is %s.' % (myMode.title(), outputFilename))​
