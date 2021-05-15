import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import json


def createdata(filename):
    with open(filename, encoding='utf-8') as f:
        fdata = json.load(f)
        fdict = {}
        for key in fdata:
            for value in fdata[key]:
                fdict[value] = key
        comments = []
        for key in fdict:
            comments.append(key)
        pubs = []
        for value in fdict.values():
            pubs.append(value)
        fdata = {'comments': comments, 'pub': pubs}
    return fdata
    
data = createdata('results.json')
data = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
data.columns = ["comments", "pub"]

training_data = data.copy()
testing_data = data.copy()

X = training_data.comments
y = training_data.pub
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 1), max_features=1000)

X_featurized = tfidf_vectorizer.fit_transform(X)

clf = LogisticRegression()
clf.fit(X_featurized, y)


comment = input('Введите комментарий: ')
new_data = {'comments': comment, 'pub': ''}
new_data = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in new_data.items()]))
new_data.columns = ["comments", "pub"]

newX = new_data.comments
newY = new_data.pub

newXfeaturized = tfidf_vectorizer.transform(newX)
new_pred = clf.predict(newXfeaturized)

print(new_pred)
