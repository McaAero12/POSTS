import datetime
import random
import string
from idlelib.rpc import request_queue
from .models import Book
from django.http import HttpResponse
from django.shortcuts import render
from .models import Game
from .models import Post

def about(request):
    return HttpResponse("Меня зовут Адилет.Я люблю  кодить !")

def now(request):
    return HttpResponse(f"Сейчас {datetime.datetime.now().strftime('%H:%M:%S')}")

def hello(request):
    name = request.GET.get("name", "Гость")
    return HttpResponse(f"Привет, {name}!")


def add(request):
    a = int(request.GET.get("a", 0))
    b = int(request.GET.get("b", 0))
    return HttpResponse(f"Сумма: {a + b}")


def joke(request):
    jokes = [
      'Байт - это укус программиста'
      'python - не только змей'
      'тостер - хлебный сервер'
    ]
    return HttpResponse(random.choice(jokes))


def password(request):
    pwd = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    return HttpResponse(f"Твой новый пароль: {pwd}")


def home(request):
    context = {"name": "Айгуль", "age": 15}
    return render(request, "main/home.html", context)

def books(request):
    context = {"books": ["Властелин колец", "1984", "Питон для детей"]}
    return render(request, "main/home.html", context)

def coin(request):
    context = {
        "name": "Адилет", "codecoin": random.randint(1, 100),
        "animals": ["Лев", "Кот", "Тигр", "Акула"],
        "points": random.randint(1, 100)
    }
    return render(request, "main/home.html", context)


def me(request):
    context = {
        "name": "Адилет",
        "age": 16,
        "city": "Бишкек",
        "hobby": ["Футбол", "Программирование", "Игры"],
    }
    return render(request, "main/home.html", context)

def book_list(request):
    books = Book.objects.all()
    return render(request, "main/book_list.html", {"books": books})

def games(request):
    games = Game.objects.all()
    return render(request, "main/games.html", {"games": games})

def posts(request):
    posts = Post.objects.all()
    return render(request, "main/post.html", {"posts": posts})