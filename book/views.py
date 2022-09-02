from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def index(request):
    b = request.user.book_set.all()
    context = {
        "bset" : b
    }
    return render(request, "book/index.html", context)

def create(request):
    if request.method == "POST":
        im = request.POST.get("impo")
        sn = request.POST.get("sname")
        su = request.POST.get("surl")
        sc = request.POST.get("scon")
        Book(maker=request.user, impo=bool(im),site_name=sn,site_url=su,site_con=sc).save()
        return redirect("book:index")
    return render(request, "book/create.html")