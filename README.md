# определение пабликов по комментариям 

*гипотеза:* паблики можно определить по словам в комментариях
для этого мы создаем облака слов (папка word clouds), исключая стоп слова

# что мы делаем:
*часть 1:*
  - скачиваем из вк комментарии из выбранных 12 пабликов (последние 100 постов)
  - делим комментарии на слова
  - выделяем стоп слова
  - приводим все к начальной форме и одинаоквому виду

*часть 2:* \n
два варианта кода для определения частотности каждого слова и вероятности встретить его в тексте


* понять, как питоном рисовать облако слов про коллекцию текстов
* превратить данные в аналогичную ^ табличку (с текстами в одной колонке, пабликами в другой)
* тоже завести X и y
* превратить X в числа
* тоже раздобыть модель, "обучить" её
* посмотреть на предсказание модели для заранее припрятанной (табличка в которой есть текст и паблик-этого-текста) доли данных
* сравнить с альтернативной программой
* посмотреть на процент коментов, на которых эта программа ошибалась (и то же с другой программой)
