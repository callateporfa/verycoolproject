import collections
import pymorphy2
import nltk
nltk.download("stopwords")
from PIL import Image  # Pillow with WordCloud to image manipulation
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords
import sys, os
import json
import string
os.chdir(sys.path[0])

morph = pymorphy2.MorphAnalyzer()

# делаем удобный для работы файл
with open('results.json', encoding='utf-8') as f:
    json_dict = json.load(f)
for key in json_dict:
    blin = []
    for value in json_dict[key]:
        value = value.split(' ')
        for word in value:
            word = morph.parse(word)[0].normal_form  # приводим слова к начальной форме
            word = word.strip(string.punctuation).lower()  # убираем пунктуацию и заглавные буквы
            blin.append(word)
    json_dict[key] = blin

# сделали и сохраняем в формате json
with open('new_res.json', 'w', encoding='utf-8') as new:
    json.dump(json_dict, new, ensure_ascii=False, indent=2)


# ищем стопслова
with open('new_res.json', 'r', encoding='utf-8') as f:
    json_dict = json.load(f)
most_common_total = []
for key in json_dict:
    c = collections.Counter()
    for value in json_dict[key]:
        value = value.split(' ')
        for word in value:
            c[word] += 1
    json_dict[key] = c
    for i in json_dict[key].most_common(10000):  # собираем список самых частотных слов в каждом паблике
        for word in i:
            if isinstance(word, str) is True:
                most_common_total.append(word)  # готовый лист стоп-слов

# нашли
res = []
for i in most_common_total:
    if most_common_total.count(i) == 12:
        res.append(i)
res = list(set(res))

new = open('new_res.json', 'r', encoding='utf-8').read()
for key in json_dict:
    text = open(str(key) + '.json', 'w+', encoding='utf-8')
    json.dump(json_dict[key], text, ensure_ascii=False, indent=2)  # json файл для каждого паблика

for key in json_dict:
    text = open(str(key) + '.json', 'r', encoding='utf-8').read()
    stoplist = list(STOPWORDS)+list(stopwords.words('russian'))+ res  # стоп-слова по умолчанию + русские стоп-слова + + стоп-слова наших данных

    wc = WordCloud(                 # параметры облака слов
        background_color='white',
        stopwords=stoplist,
        height=1000,
        width=1500)
    wc.generate(text)
    wc.to_file(str(key) + '.png')  # сохраняем картику с названием паблика
