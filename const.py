Sentence = input("Please enter your sentence: ")

print ("\n Consonants")
for Cons in 'bcdfghjklmnpqrstvwxyz ':
	if Cons in Sentence:
		print (Cons)
	
	
Sentence2 = input("Please enter your sentence: ")

print ("\n Vowels")
for Vowel in 'aeiou, AEIOU':
	if Vowel in Sentence2:
		print (Vowel)	