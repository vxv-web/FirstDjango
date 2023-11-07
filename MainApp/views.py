from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity": 5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity": 12},
   {"id": 7, "name": "Картофель фри" ,"quantity": 0},
   {"id": 8, "name": "Кепка" ,"quantity": 124}
]



def home(request):
    text = '''
        <header>
            / <a href='/'>Home</a> / <a href='/items'>Items</a> / <a href='/about'>About</a> /
        </header>
        <br>
        <h1> Home </h1>
        <h1>"Изучаем django"</h1>
        <strong>Автор</strong>: <i>Иванов И.П.</i>
        '''

    return HttpResponse(text)


def about(request):
    author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
    }
    result = f"""
    <header>
        / <a href='/'>Home</a> / <a href='/items'>Items</a> / <a href='/about'>About</a> /
    </header><br>
    <h1> About </h1>
    <br>
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br><br>

    <a href="/"> Back to Home </a> 
    """
    return HttpResponse(result)


def get_item(request, item_id):
    try:
        id = item_id
        item = [i for i in items if i['id'] == id][0]
        result = f"""
            Название: {item['name']}
            <br>
            Количество: {item['quantity']}
        """
    except:
        result = f"""Товар с id = {id} не найден"""
        
    return HttpResponse(result)

def items_list (request):
    text = '''
        <header>
            / <a href='/'>Home</a> / <a href='/items'>Items</a> / <a href='/about'>About</a> /
        </header><br>
        <h1> Items </h1>
        <ul>
    '''
    for i in items:
        text = text + f"""<li>Название: {i['name']}, количество: {i['quantity']}</li>"""
    text = text + '''
        </ul>
        <a href="/"> Back to Home </a> 
    '''
    return HttpResponse(text)