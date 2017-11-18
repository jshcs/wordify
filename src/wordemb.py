from headers import *
import utils
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import collections

def create_word_embeddings(tokens_list):
	print "Starting the embedding process...."
	word_embeddings=Word2Vec(tokens_list,min_count=1)
	vocab=list(word_embeddings.wv.vocab)
	print "Embeddings ready...."
	return word_embeddings,vocab


def check_additive(target_word,input_sentence,word_embeddings):
    input_tokens=input_sentence.split()
    target_embedding=word_embeddings[target_word]
    N=len(target_embedding)
    input_cumm_embedding=np.zeros(N)
    for token in input_tokens:
        input_cumm_embedding+=word_embeddings[token]
    print input_cumm_embedding
    mae=np.sum(np.abs(target_embedding-input_cumm_embedding))/N
    return mae

def check_multiplicative(target_word,input_sentence,word_embeddings):
    input_tokens=input_sentence.split()
    target_embedding=word_embeddings[target_word]
    N=len(target_embedding)
    input_cumm_embedding=np.ones(N)
    for token in input_tokens:
        input_cumm_embedding*=word_embeddings[token]
    print input_cumm_embedding
    mae=np.sum(np.abs(target_embedding-input_cumm_embedding))/N
    return mae

def cosine_sim(word_embedding1,word_embedding2):
	d1=np.sqrt(np.sum(word_embedding1**2))
	d2=np.sqrt(np.sum(word_embedding2**2))
	n=word_embedding1.dot(word_embedding2)
	return n/(d1*d2)

def get_most_similar(input_sentence,word_embeddings,vocab,op='additive'):
    input_tokens=input_sentence.split()
    N=len(word_embeddings[input_tokens[0]])
    #input_cumm_embedding=np.array(N)
    cs_list=[]
    if op=='additive':
        input_cumm_embedding=np.zeros(N)
        for token in input_tokens:
            input_cumm_embedding+=word_embeddings[token]
    elif op=='multiplicative':
        input_cumm_embedding=np.ones(N)
        for token in input_tokens:
            input_cumm_embedding*=word_embeddings[token]
    for v in vocab:
        cs_list.append((v,cosine_sim(input_cumm_embedding,word_embeddings[v])))
    sorted_cs_list=sorted(cs_list,key=lambda tup:tup[1],reverse=True)
    return sorted_cs_list[:5]


dictionary,wcount=utils.readdict(WNDICT)
tok,tokcount=utils.tokenize(dictionary)

word_embeddings,vocab=create_word_embeddings(tok)

sentence='to describe something vividly'
target_word='exposition'
print check_additive(target_word,sentence,word_embeddings)
print check_multiplicative(target_word,sentence,word_embeddings)
print "With additive",get_most_similar(sentence,word_embeddings,vocab)
print "With multiplicative",get_most_similar(sentence,word_embeddings,vocab,op='multiplicative')