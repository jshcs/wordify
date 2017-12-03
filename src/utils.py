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

def remove_swords(ltokens):
	res=[w for w in ltokens if w not in SWORDS]
	return res

def tokenize(dict):
	#dict is a list of (word, definitions)
	#Every word-definition pair is converted to a sentence by concatenating the word+definition
	#This sentence is tokenized to get a list of tokens for every word-definition pair
	#All such lists are appended to tok
	tok=[]
	for i,(w,d) in enumerate(dict):
		sentence=w+" "+d
		tokenized_sentence=sentence.split()
		tok.append(remove_swords(tokenized_sentence))
	return tok,len(tok)

def train_test_split(dict,ratio):
	N=len(dict)
	train_size=int(N*ratio)
	random.shuffle(dict)
	train_set=dict[:train_size]
	test_set=dict[train_size+1:]
	return train_set,test_set

def make_cumm_embeddings(input_sentence,word_embeddings,method='additive'):
	input_tokens=[w for w in input_sentence.split() if w not in SWORDS]
	N=WV_SIZE
	if method=='additive':
		res_embedding=np.zeros(N)
		for i in input_tokens:
			if i not in word_embeddings:
				continue
			res_embedding+=word_embeddings[i]
	elif method=='multiplicative':
		res_embedding=np.ones(N)
		for i in input_tokens:
			if i not in word_embeddings:
				continue
			res_embedding*=word_embeddings[i]
	return res_embedding

def cosine_sim(word_embedding1,word_embedding2):
	d1=np.sqrt(np.sum(word_embedding1**2))
	d2=np.sqrt(np.sum(word_embedding2**2))
	n=word_embedding1.dot(word_embedding2)
	return n/(d1*d2)

def get_most_similar(input_embedding,word_embeddings,vocab,return_length,op='additive'):
	cs_list=[]
	for v in vocab:
		cs_list.append((v,cosine_sim(input_embedding,word_embeddings[v])))
	sorted_cs_list=sorted(cs_list,key=lambda tup:tup[1],reverse=True)
	return sorted_cs_list[:return_length]

def get_list_from_tuple(ltuple):
	res=[]
	for i in ltuple:
		res.append(i[0])
	return res

def eval_method(test_set,vocab,word_embeddings,recall_count,method='additive'):
	hits=0
	N=len(test_set)
	cnt=0
	result_list=[]
	acc_list=[0 for x in ACC_NUMS]
	rank_list=[]
	for ip in test_set:
		cnt+=1
		target_word=ip[0]
		input_sentence=ip[1]
		input_embedding=make_cumm_embeddings(input_sentence,word_embeddings,method)
		most_similar_list=get_most_similar(input_embedding,word_embeddings,vocab,recall_count,op=method)
		result_list=get_list_from_tuple(most_similar_list)
		if target_word in result_list:
			hits+=1
		for a in range(len(ACC_NUMS)):
			if target_word in result_list[:ACC_NUMS[a]]:
				acc_list[a]+=1
		print "%f/%f done and hits: %d"%(cnt,N,hits)
		if target_word in vocab:
			rank_list.append(result_list.index(target_word))
	print "The mean rank is: %f"%(np.mean(rank_list))
	acc_list=[float(x)/float(N) for x in acc_list]
	print "The accuracy list is: ",acc_list
	return float(hits)/float(N)


