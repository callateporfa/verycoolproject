# определение пабликов по комментариям 

*гипотеза:* паблики можно определить по словам в комментариях
для этого мы создаем облака слов (папка word clouds), исключая стоп слова

# цель

программа, которая принимает на вхоод рандомный комментарий из input и определяет, в каком паблике этот комментарий мог бы находиться  с наибольшей вероятностью
# что мы делаем:
*часть 1:*
  - скачиваем из вк комментарии из выбранных 12 пабликов (последние 100 постов)
  - делим комментарии на слова
  - выделяем стоп слова
  - приводим все к начальной форме и одинаоквому виду

*часть 2:*


два варианта кода для определения частотности каждого слова и вероятности встретить его в тексте

 
первый вариант: с машинным обучением
* превратить данные из json в таблицу (колокнки - тексты комментариев и названия пабликов)
* комментарий -> число
* заводим и обучаем модель
* ссмотрим на предсказание модели для отдельной доли данных
* проверяем разные max_features в vectorizer и то, как от этого зависит точность (наиболее точное - 10000)

второй вариант: "вручную" считаем вероятности
* делим на слова, лемматизация
* список "probabilities* с 12 ячейками
* если слово есть в частотном словаре, то прибавляем почленно список вероятностей в 12 пабликах к probabilities
* домножаем полученные суммы на вероятность встретить именно этот паблик

*часть 3:*


сравнить с альтернативной программой
* посчитать процент комментов, на которых каждая программа ошибалась и понять, какая ошибается реже

# итог


работающая программа лмао реально manifesting
