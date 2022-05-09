import numpy as np
import pandas as pd
import nltk
import json
import re
import csv
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

pd.set_option('display.max_colwidth', 300)

data = []

# booksummaries.txt 파일이 너무 커서 push하지 않음, input폴더 안에 직접 넣어서 사용할 것
with open("input/booksummaries.txt", 'r', encoding='UTF-8') as f:
    reader = csv.reader(f, dialect = 'excel-tab')
    for row in tqdm(reader):
        data.append(row)
        
book_index = []
book_id = []
book_author = []
book_name = []
summary = []
genre = []
a = 1

for i in tqdm(data):
    book_index.append(a)
    a = a+1
    book_id.append(i[0])
    book_name.append(i[2])
    book_author.append(i[3])
    genre.append(i[5])
    summary.append(i[6])

df = pd.DataFrame({'Index': book_index, 'ID': book_id, 'BookTitle': book_name, 'Author': book_author,
                       'Genre': genre, 'Summary': summary})


def clean_summary(text):
    text = re.sub("\'", "", text)
    text = re.sub("[^a-zA-Z]"," ",text)
    text = ' '.join(text.split())
    text = text.lower()
    return text

df['clean_summary'] = df['Summary'].apply(lambda x: clean_summary(x))

df['GenreString'] = df['Genre'].apply(lambda x: ' '.join(x))
df["combined_text"] = df["clean_summary"] + " " + df["Author"] + " " + df["GenreString"]


# min_df = 최소 빈도값(문서의 수), analyzer = word(단어 단위로 학습) ngram_range(1, 2) = 단어 묶음 1개부터 2개까지
tf = TfidfVectorizer(analyzer = "word", ngram_range=(1,2), min_df=0, stop_words='english')

# fit = 훈련 데이터 분포 학습 transform = 스케일 조정
tfidf_matrix = tf.fit_transform(df['combined_text'])

# 코사인 유사도
cosine =  cosine_similarity(tfidf_matrix, tfidf_matrix)


def get_title_from_index(Index):
    return df[df.Index == Index]["BookTitle"].values[0]


def get_index_from_title(BookTitle):
    return df[df.BookTitle == BookTitle]["Index"].values[0]


def get_recommendations(book):
    book_index = get_index_from_title(book)
    similar_books = list(enumerate(cosine[book_index]))
    sortedbooks = sorted(similar_books, key = lambda x:x[1], reverse=True)[1:]
    i = 0
    for book in sortedbooks:
        print(get_title_from_index(book[0]) + " by " + df.Author[df["Index"] == book[0]])
        i = i+1
        if i> len(similar_books):
            break

print(get_recommendations('The Prow Beast'))