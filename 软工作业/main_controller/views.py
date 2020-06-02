from django.shortcuts import render, redirect
import room
import customer
import bill
import detailed_record
import daily_record
import weekly_record
import main_controller
import sub_controller
import screen
import server_queue
import dispatch_queue
import controller
import detailed_list_customer
import detailed_list_room

# Create your views here.
def room(request):
    return render(request,'room.html')

def administrator(request):
    return render(request,'administrator.html')

def power_on_html(request):


    return render(request,'power_on.html')

def set_default_html(request):
    return render(request,'set_default.html')

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        print(request.POST)
        u = request.POST.get('username')
        p = request.POST.get('password')
        print(u)
        print(p)
        if u =='root' and p =='123':
            return redirect('/power_on/')
        else:
            return render(request, 'login.html',{'msg':'用户名或密码错误'})





