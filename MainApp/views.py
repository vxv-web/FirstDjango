from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity": 5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity": 12},
   {"id": 7, "name": "Картофель фри" ,"quantity": 0},
   {"id": 8, "name": "Кепка" ,"quantity": 124}
]



def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.com"
    }
    return render(request, "index.html", context)


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
    for item in items:
        if item["id"] == item_id:
            context = {
                "item": item
            }
            return render(request, "item-page.html", context)
    return HttpResponseNotFound(f"Товар c id={item_id} не найден")


def items_list (request):
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)