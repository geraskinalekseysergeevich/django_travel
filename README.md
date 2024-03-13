Для развертывания сайта на локальном копьютере нужно:

1. Обновить pip
2. Установить virtualenv
pip install virtualenv
3. В корне проекта создать виртуальную среду
virtualenv venv
4. Активировать ее
source venv/bin/activate
5. Установить django в виртуальную среду
pip install django
6. В папке project активировать сервер
python manage.py runserver