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
    for i in json_dict[key].most_common(10000):
        for word in i:
            if isinstance(word, str) is True:
                most_common_total.append(word)

res = []
for i in most_common_total:
    if most_common_total.count(i) == 12:
        res.append(i)

res = list(set(res))



