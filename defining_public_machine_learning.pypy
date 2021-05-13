import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

new_data = pd.DataFrame(dict)
DataFrame(dict([ (k,Series(v)) for k,v in new_data.items() ]))

training_data = new_data.copy()
testing_data = new_data.copy()

from sklearn.feature_extraction.text import TfidfVectorizer

# векторизатор -- это штука, умеющая превращать тексты
# в наборы чисел фиксированной длины

tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 1),
                                   max_features=1000)

# ngram_range=(1, 1) -- словом считается слово 
# (а могло бы как слово, так и два слова)
# max_features=1000 -- надо как-то оставить только 1000 слов из всех


X = training_data.text
y = training_data.pub

# мы хотим, чтобы каждый коммент превратился из текста в числа
# традиционно хочется чтобы каждый комент описывался одним и тем же
# количеством чисел
X_featurized = tfidf_vectorizer.fit_transform(X)

new_data.columns = ["comments", "pub"]

clf = LogisticRegression()  # завели себе модель машинного обучения
# модель пока не знает, как быть с нашими данными
# давайте покажем ей наши данные, пусть учится:
clf.fit(X_featurized, y)

X_test_featurized = tfidf_vectorizer.transform(new_data.comments)
test_pred = clf.predict(X_test_featurized)

new_new_data = pd.DataFrame({"text": ["кошка ест еду"], "pub": ["лентач"]})
new_new_data
#тестовый материал

newX = new_new_data.text
newY = new_new_data.pub

newXfeaturized = tfidf_vectorizer.transform(newX)
new_pred = clf.predict(newXfeaturized)

newX = new_new_data.text
newY = new_new_data.pub

newXfeaturized = tfidf_vectorizer.transform(newX)
new_pred = clf.predict(newXfeaturized)

new_pred
#то что предсказывает программа
