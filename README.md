# Резервное копирование

---
Программа для резервного копирования фотографий с профиля(аватарок) пользователя VK в облачное хранилище Яндекс.Диск.
## Установка и запуск проекта
1. Клонировать проект
```
git clone https://github.com/ivangol739/profilebackup
```     
2. Перейти в каталог проекта
```
cd profilebackup
```  
3. Создать и активировать виртуальное окружение

**Windows**
```
python -m venv venv
venv\Scripts\activate
```  
**macOS и Linux**
```
python3 -m venv venv
source venv/bin/activate
```
4. Установить зависимости
```
pip install -r requirements.txt
```  
5. Настройка переменных окружения. Создать файл `.env` в корневом каталоге и добавить токены.
```
API_TOKEN_VK=токенВК
API_TOKEN_YA=токенЯн
```  
6. Запустить проект
```
python main.ru
```  