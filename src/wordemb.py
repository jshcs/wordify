from headers import *
import utils
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import collections
import spacy
from spacy.vocab import Vocab
from spacy.language import Language

def create_word_embeddings(tokens_list):
	print "Starting the embedding process...."
	word_embeddings=Word2Vec(tokens_list,min_count=1,size=WV_SIZE)
	vocab=list(word_embeddings.wv.vocab)
	print "Embeddings ready...."
	return word_embeddings,vocab


def check_additive(target_word,input_sentence,word_embeddings):
	input_tokens=input_sentence.split()
	target_embedding=word_embeddings[target_word]
	N=WV_SIZE
	input_cumm_embedding=np.zeros(N)
	for token in input_tokens:
		input_cumm_embedding+=word_embeddings[token]
	print input_cumm_embedding
	mae=np.sum(np.abs(target_embedding-input_cumm_embedding))/N
	return mae

def check_multiplicative(target_word,input_sentence,word_embeddings):
	input_tokens=input_sentence.split()
	target_embedding=word_embeddings[target_word]
	N=WV_SIZE
	input_cumm_embedding=np.ones(N)
	for token in input_tokens:
		input_cumm_embedding*=word_embeddings[token]
	print input_cumm_embedding
	mae=np.sum(np.abs(target_embedding-input_cumm_embedding))/N
	return mae


dictionary,wcount=utils.readdict(WNDICT)
train_dict,test_dict=utils.train_test_split(dictionary,SPLIT_RATIO)
tok,tokcount=utils.tokenize(train_dict)

word_embeddings,vocab=create_word_embeddings(tok)
#print len(vocab)

#print utils.eval_method(test_dict,vocab,word_embeddings,len(vocab),method='additive')
nlp=utils.readwe(SPACYWE)
nlp.vocab.vectors.resize((len(nlp.vocab.vectors),50))
print utils.eval_method_with_spacy(test_dict,vocab,nlp,100,method='additive')
