import pymorphy2
import nltk
nltk.download("stopwords")
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords
import sys, os
import json
import string
os.chdir(sys.path[0])
morph = pymorphy2.MorphAnalyzer()
with open('results.json', encoding='utf-8') as f:
    json_dict = json.load(f)
for key in json_dict:
    blin = []
    for value in json_dict[key]:
        value = value.split(' ')
        for word in value:
            word = morph.parse(word)[0].normal_form
            word = word.strip(string.punctuation).lower()
            blin.append(word)
    json_dict[key] = blin

with open('new_res.json', 'w', encoding = 'utf-8') as new:
    json.dump(json_dict, new, ensure_ascii=False, indent=2)

    stopwords = list(STOPWORDS)+list(stopwords.words('russian')) + res # res берем из new_stop_list_maker
    wc = WordCloud(
            background_color='white',
            stopwords=stopwords,
            height=800,
            width=1000
        )
    for key in json_dict:
        wc.generate(str(json_dict))
        wc.to_file(str(key)+'.png')
