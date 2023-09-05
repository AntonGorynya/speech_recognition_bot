# speech_recognition_bot

# Установка
## Получение credentials.json от Google-аккаунта
Установите консольную утилиту [gcloud](https://cloud.google.com/sdk/docs/install). Перезапустите компьютер.
После чего введите команду

```commandline
gcloud init 
```
Выполните аутентификацию в браузере.
После чего выберете ваш проект
```commandline
Pick cloud project to use:  
 [1] possible-symbol-380617 
 [2] quickstart-1571052923647
 [3] test-sheets-api-1571052007228
 [4] tg-bot-rgfd
 [5] Enter a project ID
 [6] Create a new project
Please enter numeric choice or text value (must exactly match list item):  4 

```

Для генрации credentials.json выполните
```commandline
gcloud auth application-default login
```

## Создание .env файла

Заполните переменную окружения `GOOGLE_APPLICATION_CREDENTIALS`, где лежит путь до файла с ключами от Google.
А так же `TG_TOKEN`, где лежит токен он вашего бота
