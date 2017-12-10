import spacy
from headers import *
from spacy.vocab import Vocab
from spacy.language import Language
import utils

nlp=spacy.load(EN_MODEL)
print "model loaded"
whole_thing=utils.return_whole_file(WNDICT)

print "whole thing ready"

tokens=nlp(unicode(whole_thing,"utf-8"))

with open(SPACYWE,'wb') as handle:
	pickle.dump(nlp,handle,protocol=pickle.HIGHEST_PROTOCOL)

print 'Done writing to the pickle file'
