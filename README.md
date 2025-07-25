## Задача 1  

### Условие:  

На бесконечной в обе стороны белой полоске размеченной в клеточку находятся два робота. Ровно одна из клеток на полоске - чёрная, и она находится между роботами. Вам необходимо одинаково запрограммировать обоих роботов так, чтоб они встретились. Программа состоит из нескольких строк, каждая из которых содержит ровно одну команду. 
Допустимые команды: 
1) ML - сделать шаг на клетку влево и перейти к следующей строке программы; 
2) MR - сделать шаг на клетку вправо и перейти к следующей строке программы; 
3) IF FLAG - проверить, находимся ли мы на чёрной клетке. Если да, перейти к следующей строке программы, иначе, перейти к послеследующей строке программы; 
4) GOTO N - перейти к N-й строке программы; 
На выполнение каждой из команд, кроме GOTO у робота уходит 1 секунда. GOTO выполняется мгновенно.  

### Решение:  

```arduino
1. ML
2. IF FLAG
3.   GOTO 5
4. GOTO 1
5. ML
6. GOTO 5
```

Почему это сработает:  

Наши роботы начинают двигаться влево (можно сделать и версию под движение вправо). Как только бот, находящийся справа от “флага” наступит на него, он начнет идти в сторону левого быстрее, ибо левый будет продолжать каждый раз проверять, не наступил ли он на флаг (проверка занимает 1 секунду по условию задачи) - его цикл шаги: 1 → 2 → 4, в то время как бот, наступивший на “флаг” времени на проверку терять уже не будет, ибо зациклен исключительно на повторении шагов 5 → 6  

Таким образом, **левый бот** будет идти **влево** **медленнее** - **2 секунды на шаг** (ML + IF FLAG + GOTO 1 = 1+1+0), в то время как **правый** будет тратить **на шаг 1 секунду** (ML + GOTO 5 = 1 + 0)  
  
## Задача 2  

### Условие:  

В Неправильном торговом центре установлены три непрозрачных автомата со жвачкой, на одном из которых есть наклейка «Красная», на втором — «Красная и зелёная», а на третьем — «Зелёная». Какой-то из них выдаёт красную жвачку, другой — зелёную, а оставшийся — и красную, и зелёную вперемешку. Известно, что ни одна из наклеек не верна. Как понять, что продаёт каждый автомат, купив лишь одну жвачку?  

### Решение:  

Нам нужно вытаскивать жвачку из КЗ (красная-зеленая) автомата.  

В таком случае, если мы вытащили **красную**, беря во внимание, что все автоматы врут, получаем, что в автомате **КЗ - только красные** → в автомате **К (красном) только зеленые**, а **в автомате З (зеленый) - вперемешку**  

Аналогично, если из КЗ изначально вытащили зеленую  
  
## Задача 3  

### Условие:  

Напишите на любом языке программирования следующую задачу:
1. Вытащить из апи Центробанка (пример http://www.cbr.ru/scripts/XML_daily_eng.asp?date_req=11/11/2020) данные по переводу различных валют в рубли за последние 90 дней.
2. Результатом работы программы:
- нужно указать значение максимального курса валюты, название этой валюты и дату этого максимального значения.
- нужно указать значение минимального курса валюты, название этой валюты и дату этого минимального значения.
- нужно указать среднее значение курса рубля за весь период по всем валютам.
К файлу с программой, нужно прикрепить инструкцию по запуску.

### Решение представлено в виде кода и закоммичено в этот же репозиторий  
Инструкция по запуску:  

```bash
cd *ваш путь к папке со скриптом*

pip install -r requirements.txt

python3 main.py  --cache-file "currency_ids.json" --days **90 #<-- выбор кол-ва дней**
```  

Либо запуск через колаб:  
[https://colab.research.google.com/drive/164-2GM00YluFo0l4cEXeygaSZWjTIDyi?usp=sharing](https://colab.research.google.com/drive/164-2GM00YluFo0l4cEXeygaSZWjTIDyi?usp=sharing)
