import os

inputFilename = 'plain.txt'
outputFilename = 'plain.encrypted.txt'

fileObj = open(inputFilename)
content = fileObj.read()
encrypted = ""
for letter in (content):
	if letter == " ":
		encrypted += " "

	else: 
		encrypted += chr(ord(letter) + 5)
fileObj.close()

outputFileObj = open(outputFilename, 'w')
outputFileObj.write(encrypted)
outputFileObj.close()