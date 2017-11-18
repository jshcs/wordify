from headers import *

def readdict(filename):
	print "Extracting the dictionary from %s"%(filename)
	with open(filename,'rb') as handle:
		dictionary=pickle.load(handle)

	wcount=len(dictionary)
	return dictionary,wcount

def writeemb(word_embeddings,filename):
    with open(filename,'wb') as handle:
		pickle.dump(word_embeddings,handle,protocol=pickle.HIGHEST_PROTOCOL)

	print "Done writing the word_embeddings to %s"%(filename)
    
def reademb(filename):
    print "Extracting the word_embeddings from %s"%(filename)
	with open(filename,'rb') as handle:
		word_embeddings=pickle.load(handle)

	return word_embeddings

def tokenize(dict):
	#dict is a list of (word, definitions)
	#Every word-definition pair is converted to a sentence by concatenating the word+definition
	#This sentence is tokenized to get a list of tokens for every word-definition pair
	#All such lists are appended to tok
	tok=[]
	for i,(w,d) in enumerate(dict):
		sentence=w+" "+d
		tokenized_sentence=sentence.split()
		tok.append(tokenized_sentence)
	return tok,len(tok)

