from django.http import HttpResponse
from django.shortcuts import render, redirect
from main_controller import room
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
from . import models


# Create your views here.
set_default_time = 0
serverqueuelist=[]
serverqueue = server_queue.server_queue(0,serverqueuelist)

room_num_list=[]#room_num_list是已办理入住的房间列表
bill_list=[]
detailed_record_list=[]
#customer[]=customer.customer(id,room_no,total_fee)
def room(request):
    return render(request,'room.html')

def administrator(request):
    print(serverqueuelist)
    return render(request, 'administrator.html',{'serverqueuelist':serverqueuelist})

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
        global set_default_time
        if set_default_time == 0:
            set_default_time = set_default_time + 1
            return render(request, 'set_default.html')
        else:
            if request.POST.get('default_temper') == '' or request.POST.get('feerateL') == '' or request.POST.get('feerateM') == '' or request.POST.get('feerateH') == '' :
                return render(request, 'set_default.html',{'msg':'请输入所有信息'})
            if request.POST.get('default_mode') == 'hot' and (int(default_temper) < 18 or int(default_temper) >25) :
                return render(request, 'set_default.html', {'msg': '请输入正确温度'})
            if request.POST.get('default_mode') == 'cool' and (int(default_temper) < 25 or int(default_temper) > 30):
                return render(request, 'set_default.html', {'msg': '请输入正确温度'})
            else:
                if default_speed == 'low':
                    speed = 0
                elif default_speed == 'mid':
                    speed = 1
                else:
                    speed = 2

                if default_mode == 'hot':
                    mode = 0
                else:
                    mode = 1
                for room_no in range(1,6):
                    sub_controller.set_default(mode,speed,default_temper,feerateL,feerateM,feerateH)
                    # sc=models.sub_controller_db()
                    # sc.room_no=room_no+600
                    # sc.is_check_in=False
                    # sc.is_power_on=False
                    # sc.is_start_up=False
                    # sc.mode=mode
                    # sc.speed=speed
                    # sc.target_temper=default_temper
                    # sc.current_fee=0
                    # sc.total_fee=0
                    # sc.room_no=room_no+600
                    # sc.temper=0
                    # sc.feerateL=feerateL
                    # sc.feerateM=feerateM
                    # sc.feerateH=feerateH
                    # sc.default_mode=mode
                    # sc.default_temper=default_temper
                    # sc.default_speed=speed
                    # sc.dur_time=0
                    # if sc.mode == 0:
                    #     sc.cur_rate=feerateL
                    # elif sc.mode ==1:
                    #     sc.cur_rate=feerateM
                    # else:
                    #     sc.cur_rate=feerateH
                    # sc.save()
                sclist=models.sub_controller_db.objects.all()
                for row in sclist:
                    print(row)
                return redirect('/administrator/')

            #
            # if request.POST.get('default_mode') == 'cool':
            #     if int(default_temper) < 25 or int(default_temper) > 30:
            #         return render(request, 'set_default.html', {'msg': '请输入正确温度'})
            #     else:
            #         if default_speed == 'low':
            #             speed = 0
            #         elif default_speed == 'mid':
            #             speed = 1
            #         else:
            #             speed = 2
            #
            #         if default_mode == 'hot':
            #             mode = 0
            #         else:
            #             mode = 1
            #         # print(speed)
            #         # print(mode)
            #         for room_no in range(1, 6):
            #             new_sub_controller = sub_controller.sub_controller(0, mode, speed, default_temper, 0, 0,
            #                                                                room_no + 100)
            #             # print(new_sub_controller.room_no)
            #             serverqueuelist.append(new_sub_controller)
            #         # print(serverqueue)
            #         # print(serverqueuelist)
            #         return redirect('/administrator/')

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

#前台的登录
def reception_login(request):
    if request.method=="GET":
        return render(request,'reception_login.html')
    else:
        print(request.POST)
        u = request.POST.get('username')
        p = request.POST.get('password')
        print(u)
        print(p)
        if u =='recp' and p =='aaa':
            return redirect('/reception_print/')
        else:
            return render(request, 'reception_login.html',{'msg':'用户名或密码错误'})

#前台登录后初始界面
def reception_print(request):
    return render(request,'reception_print.html')

#前台登记入住
def reception_check_in(request):
    if request.method=="GET":
        return HttpResponse('please visit us with POST')
    else:
        room_no=request.POST.get('room_num')
        flag=1
        for i in room_num_list:
            if room_no==i:
                msg='此房间已有人入住，入住失败，请换一个房间'
                flag=0
                break
        if flag==1:
            msg='此房间无人入住，入住成功'
            room_num_list.append(room_no)
        return render(request,'reception_check_in.html',{'msg':msg})

#前台登记退房
def reception_check_out(request):
    if request.method=="GET":
        return HttpResponse('please visit us with POST')
    else:
        room_no=request.POST.get('room_num')
        flag=1
        for i in room_num_list:
            if room_no==i:
                msg='退房成功'
                flag=0
                break
        if flag==1:
            msg='此房间无人入住，退房失败'
            room_num_list.remove(room_no)
        return render(request,'reception_check_out.html',{'msg':msg})

#前台打印账单界面（账单数据是我自己写的test，之后应该从bill中（数据库中）获得）
def reception_print_bill(request):
    if request.method == "GET":
        return HttpResponse('please visit us with POST')
    else:
        #test
        customer='abc'
        room_no=request.POST.get('room_num')
        print(room_no)
        total_fee=100
        print(bill_list)
        new_bill=bill.bill(customer,room_no,total_fee)
        print(new_bill)
        bill_list.append(new_bill)
        print(bill_list)
        return render(request,'reception_print_bill.html',{'bill':bill_list})

#前台打印详单界面，详单数据也是我自己写的test，之后从数据库中取
#detailed_record的输出修改了一下，之前第三次作业到第四次作业的时候被改没了
def reception_print_detail(request):
    if request.method == "GET":
        return HttpResponse('please visit us with POST')
    else:
        #test
        detail_count='1'
        room_no=request.POST.get('room_num')
        request_time='2020/06/04 13:59'
        duration='6'
        temper='20'
        speed='low'
        fee='1.5'
        new_detail_record=detailed_record.detailed_record(detail_count,room_no,request_time,duration,temper,speed,fee)
        detailed_record_list.append(new_detail_record)
        #print(detailed_record_list.detail_count)
        return render(request,'reception_print_detail.html',{'detailed_record':detailed_record_list})




