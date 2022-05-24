import nltk
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_etexts
from gutenberg.query import get_metadata

from nltk import sent_tokenize, word_tokenize
from nltk.cluster.util import cosine_distance
from nltk import PorterStemmer, LancasterStemmer, word_tokenize
from nltk.tokenize import WordPunctTokenizer


text = strip_headers(load_etext(4363)).strip()
lancaster = LancasterStemmer()
lists = []
for word in nltk.word_tokenize(text):
    lists.append(lancaster.stem(word))
    
print(lists)