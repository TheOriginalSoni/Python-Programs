#This program will help you go through all the words possible in the English language, then apply simple functions on them to extract some of those words. The functions in this one are "Words that end in ay" and "Words that Caesar shift into other words"

#Note - Either use the NLTK library below (okay-ish), or download the Enable Word list library from https://www.wordgamedictionary.com/enable/ to work with it

#from nltk.corpus import brown
#english_vocab = set(w.lower() for w in brown.words())

english_vocab=[]
f = open("/home/mantis/words code/enablewordlist.txt", "r")
for x in f:
	english_vocab.append(x.strip())

print(len(english_vocab))

english_vocab2 = set()
for x in english_vocab:
	english_vocab2.add("".join(filter(str.isalpha, x)))

print(len(english_vocab2))

def caesar(word,b):
	 z = "".join(list(map(lambda x: chr(ord(x)+b) if ord(x) + b <=122 else chr(ord(x)+b-26), [char for char in word])))
	 return z

caesarable = []
for x in english_vocab2:
	for i in range(1,26):
		x2 = caesar(x,i)
		if(x2 in english_vocab2 and x<x2):
			caesarable.append((x,x2))

print(len(caesarable))

#This list above is words that caesar into other words in english.

piggable = []
for x in english_vocab2:
	if(len(x)>2 and x[-2:]=="ay"):
		piggable.append(x)

print(len(piggable))

#This list above is words that end in -ay as they might be Pig-Latin form of other words

list2 = sorted(caesarable, key = lambda x: len(x[1]), reverse = True)

list3 = list(filter(lambda x: x if len(x[0])>=4 else None,list2))

for x in list3:
	print(x[0]+"\t"+x[1])


garb = []
for x in english_vocab2:
	if (len("".join(filter(str.isalpha, x)))<len(x)):
		garb.append(x)

print(len(garb))
