import json
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

#пробная программа которая создает словарь вида {'паблик':[список всех лемм (не сет)]}
with open('results.json', encoding='utf-8') as f:
    json_dict = json.load(f)
for key in json_dict:
    list_of_lemmas = []
    for value in json_dict[key]:
        value = value.split(' ')
        for word in value:
            word = morph.parse(word)[0].normal_form
            list_of_lemmas.append(word)
    json_dict[key] = blin
print(json_dict)
