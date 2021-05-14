import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import json

with open('results.json', encoding='utf-8') as f:
    data = json.load(f)
new_dict = {}
for key in data:
    for value in data[key]:
        new_dict[value] = key
comments = []
for key in new_dict:
    comments.append(key)

pubs = []
for value in new_dict.values():
    pubs.append(value)

data = {'comments': comments, 'pub': pubs}
data = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

training_data = data.copy()
testing_data = data.copy()

X = training_data.comments
y = training_data.pub
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 1), max_features=1000)

X_featurized = tfidf_vectorizer.fit_transform(X)

data.columns = ["comments", "pub"]

clf = LogisticRegression()
clf.fit(X_featurized, y)

with open('test_data.json', encoding='utf-8') as f:
    new_data = json.load(f)
    new_dict = {}
    for key in new_data:
        for value in new_data[key]:
            new_dict[value] = key
comments = []
for key in new_dict:
    comments.append(key)

pubs = []
for value in new_dict.values():
    pubs.append(value)
new_data = {'comments': comments, 'pub': pubs}
new_data = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in new_data.items()]))
new_data.columns = ["comments", "pub"]

newX = new_data.comments
newY = new_data.pub

newXfeaturized = tfidf_vectorizer.transform(newX)
new_pred = clf.predict(newXfeaturized)

print(new_pred)
