from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import LongToShort
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")

def home_page(request):
    
    context={
        'submitted':False,
        'error':False
    }
    
    if request.method=='POST':
        data = request.POST
        print("LONG URL:",data['longurl'])
        print("CUSTOM URL:",data['custom_name'])


        # CREATE
        try:
            obj = LongToShort(long_url= data['longurl'], short_url = data['longurl'])
            obj.save()

            # READ
            context['date']=obj.date
            context['clicks']=obj.clicks
            context['submitted']=True
            context['longurl']=data['longurl']
            context['custom_name']=request.build_absolute_uri() + data['custom_name']
        except:
            context['error']=True
    else:
        print('USER SENT A GET REQUEST')
    
    return render(request,"index.html",context)


def redirect_url(request,shorturl):
    print(request.META)
    row = LongToShort.objects.filter(short_url=shorturl)
    if len(row)==0:
        return HttpResponse('No such short url exist')
    obj = row[0]
    long_url = obj.long_url
    obj.clicks += 1
    obj.save()
    print(long_url)
    return redirect(long_url)


def all_analytics(request):
    rows = LongToShort.objects.all()
    context = {'rows':rows}
    return render(request,'all-analytics.html',context)


def task(request):
    context = {'my_name':'Ambarish','x':10}
    return render(request,'task.html',context)