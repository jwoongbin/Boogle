import numpy as np
import pandas as pd
import os
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

# booksummaries.txt 파일이 너무 커서 push하지 않음, input폴더 안에 직접 넣어서 사용할 것
"""        
data_path = 'input/booksummaries.txt'
mydata = {}
understanding = []
for line in open(data_path, encoding='utf-8'):
    understanding.append(line)
    temp = line.split("\t")
    mydata[temp[2]] = temp[6] # 잘 모르겠음 



- TaggedDocument 타입으로 전처리
train_doc2vec = [TaggedDocument((word_tokenize(mydata[t])), tags = [t]) for t in mydata.keys()]

- alpha = learning rate, epochs = 반복 횟수, dm = distributed memory
model = Doc2Vec(vector_size=50, alpha=0.025, min_count = 10, dm = 1, epochs = 100)
model.build_vocab(train_doc2vec)
model.train(train_doc2vec, total_examples=model.corpus_count, epochs = model.epochs)

- 저장
model.save("d2v.model")
"""

# 마찬가지로 d2v.model 파일이 너무 커 push하지 않음, 위의 주석처리된 부분을 직접 실행해야 작동(1회만)
# 저장 후 불러오기
model = Doc2Vec.load("d2v.model")

def recommend(text):
    new_vector = model.infer_vector(word_tokenize(text))
    sims = model.dv.most_similar([new_vector])
    return sims
    

lists = recommend('The Prow Beast')