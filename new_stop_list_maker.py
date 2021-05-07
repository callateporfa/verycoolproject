import json
import collections
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
with open('results.json', encoding='utf-8') as f:
    json_dict = json.load(f)
most_common_total = []
for key in json_dict:

    c = collections.Counter()
    for value in json_dict[key]:
            value = value.split(' ')
            for word in value:
                word = morph.parse(word)[0].normal_form
                c[word] += 1
    json_dict[key] = c
    for i in json_dict[key].most_common(100):
        for word in i:
                if isinstance(word, str) == True:
                    most_common_total.append(word)

res = []
for i in most_common_total:
    if most_common_total.count(i) == 12:
        res.append(i)
print(res)



