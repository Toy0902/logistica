from django.shortcuts import render,get_object_or_404
from blog.models import Rasmlar,Matn, Ishchilar, Xodimlar


def index(request):
    rasm = Rasmlar.objects.all()
    matn = Matn.object.all()
    ishchi = Ishchilar.objects.all()
    context = {
        "rasm": rasm,
        "matn": matn,
        "ishchi": ishchi
    }
    return render(request, "index.html", context=context)
def index_detel(request,id):
    matn = get_object_or_404(Matn,id=id)
    context = {
        "detel":matn
    }
    return render(request,'detel.html',context=context)

def about(request):
    return render(request,"about.html",context={})

def h404(request):
    return render(request,"404.html",context={})

def contact(request):
    return render(request,"contact.html",context={})

def price(request):
    return render(request,"price.html",context={})

def feature(request):
    return render(request,"feature.html",context={})

def quote(request):
    return render(request,"quote.html",context={})

def service(request):
    return render(request,"service.html",context={})

def team(request):
    return render(request,"team.html",context={})

def testimonial(request):
    return render(request,"testimonial.html",context={})
# Create your views here.

def index_detel2(request,id):
    matn = get_object_or_404(Ishchilar,id=id)
    context = {
        "detel2": matn
    }
    return render(request,'detel2.html',context=context)

def index_detel3(request,id):
    matn = get_object_or_404(Xodimlar,id=id)
    context = {
        "detel3": matn
    }
    return render(request,'detel3.html',context=context)