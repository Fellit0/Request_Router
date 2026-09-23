Сценарий	        Команда	            Ожидаемый результат	        Фактический результат	 Код завершения    Статус


Корректный          python3 src/        Результат совпадает с       Результат совпадает         0               PASS
JSON                 main.py            datasets/expected-          с datasets/expected-
                    --input datasets/   results.json по id          results.json по id
                    requests.json
                     --output src/
                     result.json

Корректный          python3 src/main      Результат совпадает       Результат совпадает с       0               PASS
csv                 .py --input datasets  с ручной проверкой на     ручной проверкой на
                    /requests.csv --      категорию и приоритет     категорию и приоритет               
                    output src/result.csv

Путь к              python3 src/main.py      Выводится текст        Выводится текст ошибки      1               PASS
отсутствующему      --input datasets/r.json  ошибки без traceback   путь к входному файлу
файлу               --output src/result.json путь к входному файлу  не существует без  
                                             не существует          traceback

Поврежденный        python3 src/main.py      Вывод текст ошибки     Выводится текст ошибки      1               FAIL
datasets/requests   --input datasets/        без traceback          в записи отсутствует
.json               requests.json            JSON синтаксически     или пусто поле id
                    --output src/result      поврежден              либо text
                    .json

запись без text     python3 src/main.py     Вывод текст ошибки      Вывод текст ошибки          1               PASS
из datasets/        --input datasets/       без traceback           без traceback в
missing-field       missing-field.json      в записи отсутствует    записи отсутствует
.json               --output src/result     или пусто поле id       или пусто поле id 
                    .json                   либо text               либо text


Расхождние в поврежденном файле произошло из-за того, что в коде ловится ошибка json.JSONDecodeError для
синтаксически поврежденному файла, но она является подклассом ошибки ValueError, которая в коде стоит выше,
поэтому сработала ошибка ValueError и вывелось не то сообщение (для редактирования нужно либо убрать ValueError
и описать для другой ошибки конкретное поле , либо перенести ValueError ниже)