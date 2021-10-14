## Запуск приложения 
```
1) docker-compose build
2) docker-compose up
3) http://127.0.0.1:8000/
```

# API documentation
## Для администратора

Все вызовы для администратора требуют базовую HTTP-авторизацию.

#### GET /api/admin/survey/

Получение списка всех опросов. Тело ответа:
```
{
    "count":, # количество объектов (int)
    "next":, # ссылка на следующую страницу (link)
    "previous":, # ссылка на предыдущую страницу (link)
    "results": [
        {
            "id":, # id опроса (int)
            "name":, # название опроса (str)
            "description":, # описание опроса (str)
            "start":, # дата начала опроса (str)
            "stop": , # дата окончания (str)
            "questions": [
                    "id":, # id вопроса в опросе (int)  
                    ---
            ]
        },
        ----
    ]
}
```

#### POST /api/admin/survey/

Создание нового опроса. Тело запроса:
```
{
    "name":, # имя опроса 
    "description":, # описание опроса
    "stop": # время окончания
}
```
#### GET /api/admin/survey/{id_survey}/

Получение подробной информации об одном опросе. Тело ответа:
```
{
    "id":, # id опроса (int)
    "name":, # название опроса (str)
    "description":, # описание опроса (str)
    "start":, # дата начала опроса (date)
    "stop":, # дата окончания (date)
    "questions": [
        {
            id # id вопроса в опросе (int) 
            ---
        },
    ---
    ]
},

```

#### DELETE /api/admin/survey/{id_survey}/

Удаление опроса.

#### PUT /api/admin/survey/{id_survey}/

Редактирование опроса. Тело запроса:
```
 {
    "id":, # id опроса (int)
    "name":, # название опроса (str)
    "description":, # описание опроса (str)
    "start":, # дата начала опроса (date)
    "stop": , # дата окончания (date)
    "questions": [
            id # id вопроса в опросе (int)  
            ---
        ]
},
```
#### POST /api/admin/questions/

Добавление нового вопроса. Тело запроса:
```
{
    "type":,# тип вопроса (str) "text", "OneAnswer", "ManyAnswer"
    "text": # текст вопроса (str)
}
```
#### GET /api/admin/questions/

Подробная информация обо всех вопросах. Тело ответа:
```
{
    "count":, # количество объектов (int)
    "next":, # ссылка на следующую страницу (link)
    "previous":, # ссылка на предыдущую страницу (link)
    "results": [
        {
            "id": ,  # id вопроса
            "type":, # тип вопроса (str) "text", "OneAnswer", "ManyAnswer"
            "text": # текст вопроса (str)
        },
        ---
    ]
}
```
#### GET /api/admin/questions/{id_questions}/
Подробная информация об одном вопросе. Тело ответа:
```
{
    "id": ,  # id вопроса
    "type":, # тип вопроса (str) "text", "OneAnswer", "ManyAnswer"
    "text": # текст вопроса (str)
}
```


#### DELETE /api/admin/questions/{id_questions}/

Удаление вопроса.

#### PUT /api/admin/questions/{id_questions}/

Изменение существующего вопроса. Тело запроса:
```
{
    "type":, # тип вопроса (str) "text", "OneAnswer", "ManyAnswer"
    "text": # текст вопроса (str)
}
```

## Для пользователя

#### GET /api/survey/

Получить список активных опросов. Тело ответа:
```
{
    "count":, # количество объектов (int)
    "next":, # ссылка на следующую страницу (link)
    "previous":, # ссылка на предыдущую страницу (link)
    "results": [
        {
            "id":, # id опроса (int)
            "name":, # название опроса (str)
            "description":, # описание опроса (str)
            "start":, # дата начала опроса (date)
            "stop":, # дата окончания (date)
            "questions":[
                id # id вопроса в опросе
                ---
            ]
        },
        ---
    ]
}
```

#### GET /api/survey/{id_survey}/

Получение подробной информации об одном опросе.
Тело ответа:
```
{
    "id":, # id опроса (int)
    "name":, # название опроса (str)
    "description":, # описание опроса (str)
    "start":, # дата начала опроса (date)
    "stop":, # дата окончания (date)
    "questions":[
        {
            "id": ,  # id вопроса
            "type":, # тип вопроса (str) "text", "OneAnswer", "ManyAnswer"
            "text": # текст вопроса (str)
        },
        ---
    ]
},
```

#### POST /api/answer/{id_survey}/

Прохождение опроса пользователем. Тело запроса:
```
{
    "user_id":, # id пользователя (int)
    "question": [
        {"id_question":, # id вопроса
         "answer": ["OneAnswer"] # тип один ответ (list)
        },
        {"id_question":, # id вопроса (int)
         "answer": ["ManyAnswer", "ManyAnswer"] # тип множественный ответ (list)
        },
        {"id_question":, # id вопроса (int)
         "answer": "text" # тип текст (str)
        },
    ]
}
```

#### GET /api/result_answer/{user_id}/

Получить пройденные пользователем опросы, с детализацией выбранных ответов.
Тело ответа:
```
{
    "count":, # количество объектов (int)
    "next":, # ссылка на следующую страницу (link)
    "previous":, # ссылка на предыдущую страницу (link)
    "results": [
        {
            "id":, # id пройденного опроса (int)
            "user_id":, # id пользователя (int)
            "survey":, # id опрос (int)
            "date_end":, # время окончания пройденного опроса (str)
            "answer_question": [
                {
                    "question": {
                        "id": ,  # id вопроса (int)
                        "type":, # тип вопроса (str) "text", "OneAnswer", "ManyAnswer"
                        "text": # текст вопроса (str)
                    },
                    "text": "" # ответ на вопрос (str)
                },
                ---
            ]
        },
        ---
}
```
