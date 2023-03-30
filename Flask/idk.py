import gzip

with gzip.open(r'D:/DATASETS/Recommendation Systems/goodreads_books.json.gz','r') as f:
    line = f.readline() #reading line by line to save memory

import json

json.loads(line) #python dictionary

def parse_fields(line):
    data = json.loads(line)
    return {
        'book_id' : data['book_id'],
        'title' : data['title_without_series'],
        'ratings' : data['ratings_count'],
        'url' : data['url'],
        'cover_image' : data['image_url']
    }

book_titles = []
with gzip.open('D:/DATASETS/Recommendation Systems/goodreads_books.json.gz','r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        fields = parse_fields(line)
        
        try:
            ratings = int(fields['ratings'])
        except ValueError:
            continue
        if ratings>15:
            book_titles.append(fields)

import pandas as pd

titles = pd.DataFrame.from_dict(book_titles)
#modifies title to minimize search space
titles['mod_title'] = titles['title'].str.replace('[^a-zA-Z0-9]','',regex = True)
titles['mod_title'] = titles['mod_title'].str.lower()
titles['mod_title'] = titles['mod_title'].str.replace('\s+','',regex=True)
titles = titles[titles['mod_title'].str.len() > 0] 

#frequency matrix
#inverse document frequency - idea is to minimise the impact of common words(inverse log)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(titles['mod_title'])

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re
def make_clickable(val):
    return '<a target="_blank" href="{}">Goodreads</a>'.format(val)
#html element for each column - styling each column

def show_image(val):
    return '<img src="{}" width=50></img>'.format(val)
def search(query,vectorizer=vectorizer):
    processed = re.sub('[^a-zA-Z0-9]','',query.lower())
    query_vec = vectorizer.transform([processed])
    similarity = cosine_similarity(query_vec,tfidf).flatten()
    indices = np.argpartition(similarity,-10)[-10:]
    results = titles.iloc[indices]
    results = results.sort_values('ratings',ascending = False)
    return results.head(5).style.format({'url':make_clickable,'cover_image': show_image})

print(search('Foundation',vectorizer))
import pickle
pickle.dump(search,open('model.pkl','wb'))
