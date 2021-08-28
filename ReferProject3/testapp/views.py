from django.shortcuts import get_object_or_404, render
from . models import Apps

# Create your views here.
def home_View(request):
    apps_list=Apps.objects.all()
    return render(request,'testapp/home.html',{'apps_list':apps_list})

def Crypto_View(request):
    crypto_list=Apps.objects.filter(category__iexact = "crypto") 
    return render(request,'testapp/crypto.html',{'crypto_list':crypto_list})

def Upi_View(request):
    upi_list=Apps.objects.filter(category__iexact = "upi")
    return render(request,'testapp/upi.html',{'upi_list':upi_list})

def Stock_View(request):
    stock_list=Apps.objects.filter(category__iexact = "stock&mutualfund")
    return render(request,'testapp/stock.html',{'stock_list':stock_list}) 

def Rummy_View(request):
    rummy_list=Apps.objects.filter(category__iexact = "rummy&fantacy")
    return render(request,'testapp/rummy.html',{'rummy_list':rummy_list})          

def app_detail_view(request,app,year,month,day):
    app=get_object_or_404(Apps,slug=app,publish__year=year,publish__month=month,publish__day=day)
    return render(request,'testapp/detail.html',{'app':app})
