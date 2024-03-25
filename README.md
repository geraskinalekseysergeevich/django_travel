Сайт сделан под разрешение 1280px.
Для развертывания сайта на локальном копьютере нужно:

1. Обновить pip
2. Установить virtualenv<br>
pip install virtualenv
3. В корне проекта создать виртуальную среду<br>
virtualenv venv
4. Активировать ее<br>
source venv/bin/activate
5. Установить django в виртуальную среду<br>
pip install django
6. В папке project активировать сервер<br>
python manage.py runserver
