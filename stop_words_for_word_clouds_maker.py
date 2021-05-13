import json
import collections

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
    #создаем словарь вида {'паблик': {частотный словарь для слов внутри всех комментариев пабликов}}
    for i in json_dict[key].most_common(10000):
        for word in i:
            if isinstance(word, str) is True:
                most_common_total.append(word)
    #создаем большой объединенный список из 10000 самых частотных слов в каждом из пабликов, т.е. в теории список из 120000 частотных слов, среди которых есть повторяющиеся 
    #(на практике он меньше, потому что не везде набирается 10000 слов...)

res = []
for i in most_common_total:
    if most_common_total.count(i) == 12:
        res.append(i)

res = list(set(res))
#создаем список слов, которые встречаются в частотном списке всех 12 пабликов, т.е. те слова, у которых есть 12 копий в большом списке  


