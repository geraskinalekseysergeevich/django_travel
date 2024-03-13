from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def posts(request):
    return render(request, 'main/posts.html')

def post1(request):
    return render(request, 'main/post1.html')

def post2(request):
    return render(request, 'main/post2.html')

def post3(request):
    return render(request, 'main/post3.html')

def calculate(request):
    result = None
    if request.method == 'POST':
        number = float(request.POST.get('number'))
        if number < 62:
            result = (number ** 2) + 4 + 5
        else:
            result = 1 / (number ** 2) + (4 * number) + 5
    return render(request, 'main/task.html', { 'result': result })

def about(request):
    my_data = {
        'name': 'Алагирова Ольга Валерьевна',
        'photo': 'main/img/about/my_photo.jpg',
        'email': 'ovalagirova@edu.hse.ru',
        'phone': '8 (909) 123-78-73',
        'program_name': 'Коммуникационный Дизайн',
        'program_description': 'Бакалаврская программа «Дизайн», открытая в 2018 году в Школе дизайна НИУ ВШЭ — Санкт-Петербург — первая программа в городе, выстроенная по принципам современного дизайн-образования.'
            'Отличительная особенность Школы дизайна — тесная связь с индустрией, проектный подход к образовательному процессу и привлечение к преподаванию специалистов-практиков, за которыми стоят выдающиеся профессиональные достижения. Со студентами работают кураторы, которые сами в ежедневном режиме вовлечены в проектную деятельность.'
            'Во время учёбы студенты пробуют свои силы в разных областях дизайна, формируют портфолио и приобретают знания, необходимые для решения сложных комплексных задач. Партнёрские связи с ведущими дизайн-студиями и культурными институциями Санкт-Петербурга позволяют студентам уже в процессе обучения работать с реальными проектами.'
            'На первом — базовом — курсе студенты изучают «язык» дизайна и получают основные дизайн-компетенции, на втором — осознанно выбирают дальнейшую специализацию и развиваются в ней, на третьем курсе — начинают заниматься брифами от реальных заказчиков, а в течение четвёртого — готовят комплексный дизайнерский проект, отвечающий актуальным требованиям индустрии.'
            'В 2024 году на программе «Дизайн» в Школе дизайна НИУ ВШЭ — Санкт-Петербург открыт набор на три профиля: «Коммуникационный дизайн», «Среда и интерьер» и «Дизайн одежды».'
    }
    people_data = [
        {
            'post': 'Руководитель',
            'name': 'Харшак Дмитрий Андреевич',
            'photo': 'main/img/about/harshak_photo.jpg',
            'email': 'dharshak@hse.ru'
        },
        {
            'post': 'Менеджер',
            'name': 'Анна Прищак',
            'photo': 'main/img/about/prishak_photo.jpg',
            'email': 'aprischak@hse.ru'
        }
    ]
    students_data = [
        {
            'name': 'Киреева Арина Александровна',
            'photo': 'main/img/about/arina_photo.jpg',
            'email': 'aakireeva@edu.hse.ru',
            'phone': '8 (999) 641-24-21'
        },
        {
            'name': 'Васильева Анна Олеговна',
            'photo': 'main/img/about/anna_photo.jpg',
            'email': 'aovasilyeva@edu.hse.ru',
            'phone': '8 (915) 744-99-20'
        }
    ]

    return render(request, 'main/about.html', { 'data': my_data, 'people': people_data, 'students': students_data })
