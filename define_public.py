import pymorphy2
morph = pymorphy2.MorphAnalyzer()

data = input('Введите комментарий: ')
data = data.split(' ').strip(string.punctuation).lower()

probabilities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for word in data:
    word = morph.parse(word)[0].normal_form
    if word in json_freq_dic: 
        for value in json_freq_dic[word]:
            for i in range(12):
                probabilities[i] += value[i]
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

print('Вероятно, это паблик номер ' int(probabilities.index(max(probabilities)))+1)