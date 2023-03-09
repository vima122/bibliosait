from django.shortcuts import render
from django.http import HttpResponse
from .forms import loginuser,loginbook
from .models import logindata,bookdata
import random
colvo = 0
def login(request):
    if request.method == "POST":
        login = request.POST.get("login")
        passw = request.POST.get("password")
        data = logindata.objects.get(id=1)
        if login == data.login and passw == data.password:
            return HttpResponse("<a href='home'><button>Подтверждение</button></a>")
        else:
            return HttpResponse("<a href=''><button>Неверно</button></a>")
    else:
        userform = loginuser()
        return render(request, "index.html", {"form": userform})
def home(request):
    count = 1#bookdata.objects.all().count()
    book1 = bookdata.objects.get(id=random.randint(1,count))
    book2 = bookdata.objects.get(id=random.randint(1,count))
    book3 = bookdata.objects.get(id=random.randint(1,count))
    book4 = bookdata.objects.get(id=random.randint(1,count))
    book5 = bookdata.objects.get(id=random.randint(1,count))
    book6 = bookdata.objects.get(id=random.randint(1,count))
    book7 = bookdata.objects.get(id=random.randint(1,count))
    book8 = bookdata.objects.get(id=random.randint(1,count))
    book9 = bookdata.objects.get(id=random.randint(1,count))
    book10 = bookdata.objects.get(id=random.randint(1,count))
    book11 = bookdata.objects.get(id=random.randint(1,count))
    book12 = bookdata.objects.get(id=random.randint(1,count))
    book13 = bookdata.objects.get(id=random.randint(1,count))
    book14 = bookdata.objects.get(id=random.randint(1,count))
    book15 = bookdata.objects.get(id=random.randint(1,count))
    data = {"name1": book1.name, "name2": book2.name,
     "name3": book3.name, "name4": book4.name,
      "name5": book5.name, "name6": book6.name,
       "name7": book7.name, "name8": book8.name,
        "name9": book9.name, "name10": book10.name,
         "name11": book11.name, "name12": book12.name,
          "name13": book13.name, "name14": book14.name,
           "name15": book15.name,"photo1": book1.photo,
           "photo2": book2.photo,"photo3": book3.photo,
           "photo4": book4.photo,"photo5": book5.photo,
           "photo6": book6.photo,"photo7": book7.photo,
           "photo8": book8.photo,"photo9": book9.photo,
           "photo10": book10.photo,"photo11": book11.photo,
           "photo12": book12.photo,"photo13": book13.photo,
           "photo14": book14.photo,"photo15": book15.photo}
    return render(request, "home.html", context=data)
def book(request,bookname):
    db = bookdata.objects.get(name=bookname)
    data = {"name": db.name, "names": db.names, "avtor": db.avtor, "janr": db.janr, "star": db.star, "place": db.place, "about": db.aboutbook, "photo": db.photo}
    return render(request, "book.html", context=data)
def new(request):
    if request.method == "POST":
        book = bookdata.objects.create(name=request.POST.get("name"), names=request.POST.get("names"),
        avtor=request.POST.get("avtor"), janr=request.POST.get("janr"), star=request.POST.get("star"),
        place=request.POST.get("place"), aboutbook=request.POST.get("aboutbook"), photo=request.POST.get("photo"))
        form = loginbook(request.POST, request.FILES)
        return HttpResponse("<a href='home'><button>Подтверждение</button></a>")
        #if form.is_valid():
            #form.save()
    else:
        userform = loginbook()
        return render(request, "new.html", {"form": userform})
