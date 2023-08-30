from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
                # name of input = 'check
    if  request.method == 'POST':
        check_ = request.POST['check']
        print (check_)

    date = datetime.datetime.now()
    print("test function is called")
    # return HttpResponse("<h1>hello client at {}</h1>".format(str(date)))
    isActive = True
    name= "Arth Gupta"
    list_of_program=[
        "WAP program one",
        "WAP program 2",
        "WAP program 3",
    ]
    student = {
        "st_name" :"don",
        "st_college":"medcaps"    }
    
    data = {
        "date":date,
        "isActive":isActive,
        "name":name,
        "list_of_program":list_of_program,
        "student_data":student

    }
    return render(request,"home.html",data)

def about(request):
    # return HttpResponse("<h1>hello client at about</h1>")
    return render(request,"about.html",{"title":"arth gupta"})

def service(request):
    # return HttpResponse("<h1>hello client at services</h1>")
    return render(request,"service.html",{"title":"arth gupta"})