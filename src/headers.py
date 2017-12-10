import numpy as np
import math
import pickle
import random
import scipy

WNDICT='../data/wordnetdict.pickle'
WNEMB='../data/wordnetemb.pickle'
SPLIT_RATIO=0.999
WV_SIZE=50
SWORDS=['to','a','for','the','is','of','are','they','them','their']
ACC_NUMS=[500,1000,5000,10000]
EN_MODEL='en_vectors_web_lg'
SPACYWE='../data/spacywe.pickle'