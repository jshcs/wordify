from headers import *
from nltk.corpus import wordnet as wn

def makedict():
	dictionary=[]
	print "Starting the process...."
	count=0
	for w in wn.all_synsets():
		word=w.name()
		word=word[:-5]
		definition=w.definition()
		dictionary.append((str(word),str(definition)))
		count+=1
	print "Done making the dictionary...."
	print
	return dictionary,len(dictionary)

def writedict(filename):
	dictionary,wcount=makedict()
	with open(filename,'wb') as handle:
		pickle.dump(dictionary,handle,protocol=pickle.HIGHEST_PROTOCOL)

	print "Done writing the dictionary to %s"%(filename)

writedict(WNDICT)
