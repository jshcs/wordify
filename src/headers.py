import numpy as np
import math
import pickle
import random

WNDICT='../data/wordnetdict.pickle'
WNEMB='../data/wordnetemb.pickle'
SPLIT_RATIO=0.999
WV_SIZE=50
SWORDS=['to','a','for','the','is','of','are','they','them','their']
ACC_NUMS=[500,1000,5000,10000]