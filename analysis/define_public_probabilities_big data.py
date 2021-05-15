import collections
import json
import string
'''import pymorphy2
morph = pymorphy2.MorphAnalyzer()'''
#создаем частотный словарь в виде {'слово в начальной форме': [сколько раз встречается в паблике 1, паблике 2, ... паблике12]
with open('results.json', encoding='utf-8') as f:
    json_dict = json.load(f)
most_common_total = []
for key in json_dict:
    c = collections.Counter()
    for value in json_dict[key]:
            value = value.split(' ')
            for word in value:
                '''word = morph.parse(word)[0].normal_form'''
                c[word] += 1
    json_dict[key] = c
json_freq_dict = {}
with open('new_res.json', encoding = 'utf-8') as f:#это файл со всеми словами в н.ф. который делала Арина для облаков
    data = json.load(f)
data = list(data)
for word in data:
    freq = []
    for key in json_dict:
        if word in json_dict[key]:
            freq.append(json_dict[key][word])
        else:
            freq.append(0) 
    json_freq_dict[word] = freq


import json
with open('test_data.json', encoding='utf-8') as f:
    new_data = json.load(f)
new_dict = {}
for key in new_data:
    for value in new_data[key]:
        new_dict[value] = key
c = 0
for key in new_dict:
    c += 1
print(c)

comments = []
for key in new_dict:
    comments.append(key)
#словарь вида комментарий : паблик

#основная часть
probabilities_total = []
for comments in new_dict:
    probabilities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    comments = comments.split(' ')
    for word in comments:
        word = word.strip(string.punctuation).lower()
        '''word = morph.parse(word)[0].normal_form'''
        if word in json_freq_dict: 
            for i in range(12):
                probabilities[i] += json_freq_dict[word][i] 
    probabilities_total.append(probabilities)  
         
for probabilities in probabilities_total:    
    probabilities[0] = probabilities[0]*3435/88033
    probabilities[1] = probabilities[1]*11902/88033
    probabilities[2] = probabilities[2]*11807/88033
    probabilities[3] = probabilities[3]*7686/88033
    probabilities[4] = probabilities[4]*6259/88033
    probabilities[5] = probabilities[5]*3995/88033
    probabilities[6] = probabilities[6]*7465/88033
    probabilities[7] = probabilities[7]*18251/88033
    probabilities[8] = probabilities[8]*5163/88033
    probabilities[9] = probabilities[9]*3549/88033
    probabilities[10] = probabilities[10]*5709/88033
    probabilities[11] = probabilities[11]*2812/88033

numbers_list = []
for probabilities in probabilities_total:
    number = probabilities.index(max(probabilities)) + 1
    numbers_list.append(number)

names = []
for number in numbers_list:
    if number == 1:
        names.append('Типография НИУ ВШЭ')
    if number == 2:
        names.append('Медуза')
    if number == 3:
        names.append('Лентач')
    if number == 4:  
        names.append('Капризный ленгвист')
    if number == 5: 
        names.append('Постнаука')
    if number == 6: 
        names.append('CLIQUE')
    if number == 7:
        names.append('КБ ')
    if number ==  8:
        names.append('калик)')
    if number == 9:
        names.append('абстрактные мемы для элиты всех сортов | АМДЭВС')
    if number ==  10:
        names.append('4ch')
    if number == 11:
        names.append('реализм кухонной раковины')
    if number ==  12:
        names.append('астрофотография')
print(len(names))