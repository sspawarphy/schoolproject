from django.shortcuts import render
import datetime
import pytz
# Create your views here.
def welcome(request):
    date= datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%d/%m/%Y, %H:%M:%S")
    my_dic={'date':date}
    return render(request,'studentinfoapp/welcome.html',context=my_dic)
def registration(request):
    date= datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%d/%m/%Y, %H:%M:%S")
    my_dic={'date':date}
    return render(request,'studentinfoapp/registration.html',context=my_dic)
def base(request):
    return render(request,'studentinfoapp/registration.html')
