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
set_default_time = 0
def room(request):
    return render(request,'room.html')

def administrator(request):
    return render(request,'administrator.html')

def power_on_html(request):


    return render(request,'power_on.html')

def set_default_html(request):
    if request.method == "GET":
        return render(request,'set_default.html')
    else:
        default_temper = request.POST.get('default_temper')
        default_speed = request.POST.get('default_speed')
        default_mode = request.POST.get('default_mode')
        feerateL = request.POST.get('feerateL')
        feerateM = request.POST.get('feerateM')
        feerateH = request.POST.get('feerateH')
        print(default_temper)
        print(default_speed)
        print(default_mode)
        print(feerateL)
        print(feerateM)
        print(feerateH)
        global set_default_time
        if set_default_time == 0:
            set_default_time = set_default_time + 1
            return render(request, 'set_default.html')
        else:
            if request.POST.get('default_temper') == '' or request.POST.get('feerateL') == '' or request.POST.get('feerateM') == '' or request.POST.get('feerateH') == '' :
                return render(request, 'set_default.html',{'msg':'请输入所有信息'})
            if request.POST.get('default_mode') == 'hot':
                if int(default_temper) < 18 or int(default_temper) >25:
                    return render(request, 'set_default.html', {'msg': '请输入正确温度'})
                else:
                    return redirect('/administrator/')


            if request.POST.get('default_mode') == 'cool':
                if int(default_temper) < 25 or int(default_temper) > 30:
                    return render(request, 'set_default.html', {'msg': '请输入正确温度'})
                else:
                    return redirect('/administrator/')

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





