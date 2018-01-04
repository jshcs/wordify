import numpy as np
import math
import pickle
import random
import scipy
from spacy.vocab import Vocab
from spacy.language import Language
from spacy.strings import StringStore
import spacy

WNDICT='../data/wordnetdict.pickle'
WNEMB='../data/wordnetemb.pickle'
SPLIT_RATIO=100
WV_SIZE=100
SWORDS=['to','a','for','the','is','of','are','they','them','their']
ACC_NUMS=[500,1000,5000,10000]
EN_MODEL='en_vectors_web_lg'
SPACYWE='../data/spacywe.pickle'

BIN_VALS=[500,1000,5000,10000]
DEF_LEN=10

#VOCAB_SIZE=500000

nlp=spacy.load(EN_MODEL)
removed = nlp.vocab.vectors.resize((len(nlp.vocab.vectors), WV_SIZE))
global_vocab=set([x for x in nlp.vocab.strings])
