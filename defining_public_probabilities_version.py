import collections
import json
import string
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
#создаем частотный словарь в виде {'слово в начальной форме': [сколько раз встречается в паблике 1, паблике 2, ... паблике12]:
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
json_freq_dict = {}
with open('new_res.json', encoding = 'utf-8') as f:#это файл со всеми словами в н.ф. построчным списком просто в текстовом формате формате, который делался для облаков
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

#основная часть
data = input('Введите комментарий: ')
data = data.split(' ')
for word in data:
    word = word.strip(string.punctuation).lower()
#приводим слова в инпутном комментарии к лемме и если слово есть в нашем частотном словаре, то мы берем список частотностей в 12 пабликах и прибавляем его почленно к probabilities (похоже на сложение столбиком)
probabilities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for word in data:
    word = morph.parse(word)[0].normal_form
    if word in json_freq_dict: 
        for i in range(12):
            probabilities[i] += json_freq_dict[word][i] 

#каждую из полученных сумм вероятностей домножаем на коэффициент встречаемости паблика (т.е. количество слов из комментариев этого паблика в наших данных / сумма всех слов во всех комментариях)
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

#ищем номер паблика, у которого полученная вероятность получилась максимальной и присваиваем каждому номеру название
number = probabilities.index(max(probabilities)) + 1
if number == 1:
    name = 'Типография НИУ ВШЭ'
if number == 2:
    name = 'Медуза'
if number == 3:
    name = 'Лентач'
if number == 4:  
    name = 'Капризный ленгвист'
if number == 5: 
    name = 'Постнаука'
if number == 6: 
    name = 'CLIQUE'
if number == 7:
    name = 'КБ '
if number ==  8:
    name =  'калик)'
if number == 9:
    name = 'абстрактные мемы для элиты всех сортов | АМДЭВС'
if number ==  10:
    name = '4ch'
if number == 11:
    name = 'реализм кухонной раковины'
if number ==  12:
    name = 'астрофотография'
    
print('Вероятно, это паблик номер ', number, ',', name)
