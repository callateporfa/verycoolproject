import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
# это то, что, умеет превращать тексты в наборы чисел фиксированной длины
import json


#создаем данные удобные для создания таблички
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
data = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))#создаем тебличку
data.columns = ["comments", "pub"] #переименовываем колонки таблицы

training_data = data.copy()
testing_data = data.copy()

X = training_data.comments
y = training_data.pub
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 1), max_features=1000)
# ngram_range=(1, 1) -- словом считается слово 
# (а могло бы как слово, так и два слова)
# max_features=1000 -- надо как-то оставить только 1000 слов из всех

X_featurized = tfidf_vectorizer.fit_transform(X)

clf = LogisticRegression()
clf.fit(X_featurized, y)


#приводит тестовые данные в нужный вид и тоже создаем табличку
new_data = createdata('test_data.json')
new_data = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in new_data.items()]))
new_data.columns = ["comments", "pub"]

newX = new_data.comments
newY = new_data.pub

newXfeaturized = tfidf_vectorizer.transform(newX)
new_pred = clf.predict(newXfeaturized)
#предсказываем паблики

print(new_pred)
