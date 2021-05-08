import pymorphy2
from wordcloud import WordCloud, STOPWORDS
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

    stopwords = STOPWORDS
    res = ['не', '', 'как', 'только', 'вы', 'за', 'я', 'же', 'но', 'бы', 'этот', 'а', 'для', 'то', 'с', 'на', 'в', 'из', 'так', 'ещё', 'и', 'это', 'у', 'по', 'такой', 'всё', 'быть', 'что']
    stopwords.update(res)
    wc = WordCloud(
            background_color='white',
            stopwords=stopwords,
            height=800,
            width=1000
        )
    for key in json_dict:
        wc.generate(str(json_dict))
        wc.to_file(str(key)+'.png')
