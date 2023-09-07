# speech_recognition_bot

# Установка
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```commandline
pip install -r requirements.txt
```

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
Необходимо заполнить `.env` файл вида
```commandline
TG_TOKEN='xxxx'
PROJECT_ID='xxx'
GOOGLE_APPLICATION_CREDENTIALS='xxxx'
VK_TOKEN='xxx'
TELEGRAM_LOG_BOT_TOKEN='Токен от лог бота хххх:yyyy'
LOG_CHAT_ID = 'ID вашего чата в телеграмме'
```
- `GOOGLE_APPLICATION_CREDENTIALS` где лежит путь до файла с ключами от Google.
- `TG_TOKEN`, лежит токен он вашего бота
- `PROJECT_ID` ID Вашего проекта

Токены для Телеграм ботов вы можете получить https://telegram.me/BotFather
Для получения CHAT_ID напишите любое сообщение вашему боту, после чего перейдите по ссылке https://api.telegram.org/bot{TG_TOKEN}/getUpdates

## Обучение модели
Перед первым запуском обучите модель dialogflow выполнив
```commandline
python learning_script.py
```