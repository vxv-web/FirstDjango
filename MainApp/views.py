from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.com",
        "pagename": "home"
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
    <title> About </title>    
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
        item = Item.objects.get(id=item_id)
        colors = item.colors.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар c id={item_id} не найден")
    else:
        context = {
            "item": item,
            "pagename": "item page",
            "colors": colors
        }
        return render(request, "item-page.html", context)


def items_list (request):
    items = Item.objects.all()
    context = {
        "items": items,
        "pagename": "items list"
    }
    return render(request, "items-list.html", context)