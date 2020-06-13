from django.shortcuts import render, redirect
from air_condition_system import room
from air_condition_system import customer
from air_condition_system import bill
from air_condition_system import detailed_record
from air_condition_system import daily_record
from air_condition_system import weekly_record
from air_condition_system import main_controller
from air_condition_system import sub_controller
from air_condition_system import screen
from air_condition_system import server_queue
from air_condition_system import dispatch_queue
from air_condition_system import controller
from air_condition_system import detailed_list_customer
from air_condition_system import detailed_list_room
from . import serializers,models
# Create your views here.
from django.utils import  timezone
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.db.models import Sum
import time



# Create your views here.
set_default_time = 0
room_num_list=[]#room_num_list是已办理入住的房间列表
bill_list=[]
detailed_record_list=[]

def room(request):
    return render(request,'room.html')

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('password')
        if u =='root' and p =='123':
            return redirect('/administrator/power_on/')
        else:
            return render(request, 'login.html',{'msg':'用户名或密码错误'})

def power_on(request):
    global set_default_time
    set_default_time = 0
    res = models.main_controller_db.objects.filter(id = 1)
    if res.count() == 0:
        mc = models.main_controller_db()
        mc.state = 0 #进入设置状态
        mc.save()
    else:
        res.update(state=0)
    res = {'code': 200,"message": "","data": {'state': 0}}
    return render(request, 'power_on.html', res)

def set_parameter(request):
    if request.method == "GET":
        print("in get")
        return render(request,'set_parameter.html')
    else:
        print("in post")
        default_temper = request.POST.get('default_temp')
        default_speed = request.POST.get('default_speed')
        default_mode = request.POST.get('mode')
        feerateL = request.POST.get('low_rate')
        feerateM = request.POST.get('mid_rate')
        feerateH = request.POST.get('high_rate')
        room_num = request.POST.get('room_num')
        allow_num = request.POST.get('allow_num')
        global set_default_time
        print(default_temper)
        if set_default_time == 0:
            set_default_time = set_default_time + 1
            print("first time")
            return render(request, 'set_parameter.html')
        else:
            print("more time")
            if request.POST.get('default_temper') == '' or request.POST.get('feerateL') == '' or request.POST.get('feerateM') == '' or request.POST.get('feerateH') == '' :
                return render(request, 'set_parameter.html',{'msg':'请输入所有信息'})
            if request.POST.get('default_mode') == 'hot' and (int(default_temper) < 18 or int(default_temper) >25) :
                return render(request, 'set_parameter.html', {'msg': '请输入正确温度'})
            if request.POST.get('default_mode') == 'cool' and (int(default_temper) < 25 or int(default_temper) > 30):
                return render(request, 'set_parameter.html', {'msg': '请输入正确温度'})
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
                sub_controller.set_default(mode,speed,default_temper,feerateL,feerateM,feerateH)
                main_controller.set_default(mode,speed,default_temper,feerateL,feerateM,feerateH,1,room_num,allow_num)
                return redirect('/administrator/start_up/')

def start_up(request):
    try:
        data={
            'state':1
        }
        res={
            'code':200,
            'message':'',
            'data':data,
        }
        return render(request,'start_up.html',{'res':res})
    except Exception as e:
        return JsonResponse({'code': 500, 'msg': "请求异常" + str(e)})

def check_room_state(request):
    try:
        sc = models.sub_controller_db.objects.all().order_by('room_no')
        money = models.Money.objects.all().order_by('room_no')
        data = []
        index=0
        for room in sc:
            dic={
                'room_id':room.room_no,
                'is_check_in':room.is_check_on,
                'is_power_on':room.is_power_on,
                'is_start_up':room.is_start_up,
                'wind_speed':room.speed,
                'cur_temp':room.temper,
                'target_temp':room.target_temper,
                'cur_rate':room.cur_rate,
                'cur_cost':money[index].Lmoney,
                'dur_time':room.dur_time,
            }
            data.append(dic)
            index=index+1
        res={
            'code':200,
            'message':'',
            'data':data,
        }
        return  render(request,'check_room_state.html',{'res',res})
    except Exception as e:
        return JsonResponse({'code': 500, 'msg': "请求异常" + str(e)})

def power_off(request):
    try:
        res = {
            'code':200,
            'message':'',
            'data':'',
        }
        return render(request, 'power_off.html',{'res':res})
    except Exception as e:
        return JsonResponse({'code': 500, 'msg': "请求异常" + str(e)})

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

def customer_power_on(request):
    if request.method == 'POST':
        try:
            room_id = request.POST.get('room_id')
            print(str(room_id))
            sc = models.sub_controller_db.objects.filter(room_no=room_id)
            if sc.count()==0:#如果输入了一个不存在的房间号，则返回一个错误
                print("error")
                return JsonResponse({'code': 500})
            else:
                #首先先来计数
                last_count = models.count.objects.filter(room_id=room_id).first().open_time
                models.count.objects.filter(room_id=room_id).update(open_time=last_count+1)
                #计数完毕
                sc = sc[0]
                data = {
                    'is_check_in':sc.is_check_in,
                    'mode':sc.mode,
                    'top_temp':sc.top_temp,#这个之后你加到sc里去
                    'bottom_temp':sc.bottom_temp,
                    'default_temp':sc.default_temper,
                    'default_speed':sc.default_speed,
                    'default_rate':sc.cur_rate,
                }
                sc.is_power_on = True
                sc.save()
                #创建Record表的第一条记录
                new_record = models.Record()
                new_record.StartDeta = timezone.now()
                new_record.Room = room_id
                new_record.DangDu = sc.default_temper
                new_record.Pattern = sc.mode
                new_record.Speed = sc.default_speed
                new_record.State = "开机"
                new_record.feerate = sc.cur_rate
                new_record.save()
                return JsonResponse({'code': 200, 'data': data})
        except Exception as e:
            return JsonResponse({'code': 500, 'msg': "请求异常" + str(e)})

def customer_power_off(request):
    if request.method == 'POST':
        try:
            room_no = request.POST.get('room_id')
            print(room_no)
            cur_time = timezone.now()
            controller.power_off(room_no, cur_time)
            sc = models.sub_controller_db.objects.filter(room_no=room_no)
            sc.update(is_power_on=False)
            return JsonResponse({'code': 200})
        except Exception as e:
            return JsonResponse({'code': 500, 'msg': "请求异常" + str(e)})

def room_request(request):
    if request.method == 'POST':
        try:
            room_id = request.POST.get('room_id',None)
            cur_temp = request.POST.get('cur_temp',None)
            sc = models.sub_controller_db.objects.filter(room_no=room_id)
            if sc.count() == 0:
                return JsonResponse({'code': 500, 'msg': "请求异常"})
            else:
                controller.power_on(room_id)
                sc.update(temper=cur_temp)
                sc.update(is_out_queue=False)
            return JsonResponse({'code': 200})
        except Exception as e:
            return JsonResponse({'code': 500, 'msg': "请求异常" + str(e)})

def change_target_temp(request):#改变温度是需要比较是否直接关机，这个工作一会别忘了
    if request.method == 'POST':
        try:
            # 这里有记录相关的函数
            room_no = request.POST.get('room_id')
            target_temp = request.POST.get('target_temp')
            #首先先来计数
            last_count=models.count.objects.filter(room_id=room_no).first().change_temper_time
            models.count.objects.filter(room_id=room_no).update(change_temper_time=last_count+1)
            #计数完毕
            controller.change_target_temper(room_no,target_temp)
            #接下来判断是否需要直接停止服务，根据该机器当前模式，判断室温与目标温度的关系，若需要关机，则直接将is_out_queue置为1
            last_record = models.sub_controller_db.objects.filter(room_no=room_no).first()
            cur_temp = last_record.temper#当前室温
            mode = last_record.mode
            if (mode == 0 and cur_temp <= target_temp) or (mode == 1 and cur_temp >= target_temp):#达到了停机条件
                if server_queue.if_in_sq(room_no)==True:#如果在服务队列里（需要出队列，并从调度队列中调度一台机器）
                    #需要补上调度一台机器的代码
                    controller.power_off(room_no,timezone.now())
                    last_record.update(is_power_on=True)
                last_record.update(is_out_queue = True)
            return JsonResponse({'code': 200})
        except Exception as e:
            return JsonResponse({'code': 500, 'msg': "请求异常" + str(e)})

def change_target_speed(request):
    if request.method == 'POST':
        try:
            # 这里应该有调度相关的函数
            room_no = request.POST.get('room_id')
            target_speed = request.POST.get('target_speed')
            # 首先先来计数
            last_count = models.count.objects.filter(room_id=room_no).first().change_speed_time
            models.count.objects.filter(room_id=room_no).update(change_speed_time=last_count + 1)
            # 计数完毕
            #首先应该形成一条新的记录
            controller.change_speed(room_no,target_speed)
            return JsonResponse({'code': 200})
        except Exception as e:
            return JsonResponse({'code': 500, 'msg': "请求异常" + str(e)})


def loop(request):
    if request.method == 'POST':
        try:
            room_no = request.POST.get('room_id')
            target_temp = request.POST.get('target_temp')
            sc = models.sub_controller_db.objects.filter(room_no=room_no).first()
            state = 0
            if sc.is_start_up == True:  # 在服务队列
                state = 3
            elif sc.is_out_queue == True:  # 证明他即不在服务队列，也不在等待队列
                state = 1
            else:
                state = 0
            #如果空调当前是被服务的状态，才需要进行这些加减值的操作
            if state == 3:
                speed = sc.speed
                change_rate=0
                fee_rate = 0#实际上fee_rate和change_rate在秒维度上是相同的，因为1元每度
                if speed == 0:#转换为度/秒
                    change_rate=1/180
                    fee_rate=1/180
                elif speed == 1:
                    change_rate=1/120
                    fee_rate = 1 / 120
                else:
                    change_rate=1/60
                    fee_rate = 1 / 60
                cur_temp = sc.temper
                if sc.mode == 0:#如果是制冷模式，则温度减
                    cur_temp = cur_temp - change_rate
                else:
                    cur_temp = cur_temp +change_rate
                sc.temper =cur_temp
                sc.save()

                mon = models.Money.objects.filter(Room=room_no).first()
                last_cost = mon.Lmoney
                cur_cost = last_cost + fee_rate
                mon.Lmoney = cur_cost
                mon.save()
                data={
                    'state':state,
                    'cur_cost':cur_cost,
                    'cur_temp':cur_temp,
                }
            else:#否则的话，只需要显示当前值不变即可
                cur_temp = sc.temper
                cur_cost = models.Money.objects.filter(Room=room_no).first().Lmoney
                data = {
                    'state': state,
                    'cur_cost': cur_cost,
                    'cur_temp': cur_temp,
                }

            #在这之前已经搞完了所有的返回值

            #接下来，需要完成我们每个循环必做的工作，包括：检查平时调度，给每个从控机的计时器加一（从控机的状态：开机，且在队列）
            # #计时器加一：
            # sc = models.sub_controller_db.objects.filter(is_power_on=True).filter(is_out_queue=False)
            # for item in sc:
            #     last_timer = item.dur_time
            #     item.update(dur_time=(last_timer+1))
            #计时器加一的操作应该只对本机器完成，因为当多台机器在运行时肯定不能每台机器都把所有机器加了
            sc = models.sub_controller_db.objects.filter(room_no=room_no).filter(is_power_on=True).filter(is_out_queue=False)
            if sc.count() != 0:
                sc=sc[0]
                last_timer = sc.dur_time
                new_timer=last_timer+1
                sc.dur_time = new_timer
                sc.save()
            #平时调度：
            dq = models.dispatch_queue_db.objects.all()
            if(dq.count() != 0):#调度队列不为空才有可能发生平时调度
                dq = models.sub_controller_db.objects.filter(is_power_on=True).filter(is_start_up=False).filter(is_out_queue=False).order_by("-speed","-dur_time").first()
                sq = models.sub_controller_db.objects.filter(is_start_up=True).order_by("speed","-dur_time").first()
                if dq.speed == sq.speed:#只有风速相等，才有可能发生平时调度
                    if sq.dur_time >= 120:
                        server_queue.out_queue(sq.room_no)
                        dispatch_queue.in_queue(sq.room_no)
                        dispatch_queue.out_queue(dq.room_no)
                        server_queue.in_queue(dq.room_no)


            return JsonResponse({'code': 200, 'data': data})
        except Exception as e:
            return JsonResponse({'code': 500, 'msg': "请求异常" + str(e)})
