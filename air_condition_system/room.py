from django.shortcuts import render, redirect
import json
from . import models
from django.utils import timezone



def set_room(room_no):
    return 0

def set_default_check_room(self,room_num):
    room_count = models.check_room.objects.aggregate(count=Count('room_no'))
    if room_count != 0:
        all_messages=models.check_room.objects.all()
        all_messages.delete()
    for i in range(1,room_num+1):
        mcr = models.check_room()
        mcr.room_no = i + 600
        mcr.is_check_in = False
        mcr.save()

def room_target_temper_alter_amount(mode,time,room_no):
    last_record=models.Record.objects.filter(room=room_no).first()
    last_record.update(LeaveDate=timezone.now())
    last_record.update(Date=(last_record.LeaveDate-last_record.StartDate))
    obj=models.Record(room=last_record.room,DangDu=mode,Pattern=last_record.Pattern,Speed=last_record.Speed,State=last_record.State,StartDate=timezone.now(),feerate=last_record.feerate)
    obj.save()
    return 0

def room_speed_alter_amount_plus(mode,time,room_no):
    last_record = models.Record.objects.filter(room=room_no).first()
    last_record.update(LeaveDate=timezone.now())
    last_record.update(Date=(last_record.LeaveDate - last_record.StartDate))
    feerate=0
    if mode == 0:
        feerate=0.33
    elif mode == 1:
        feerate=0.5
    else:
        feerate=1
    obj = models.Record(room=last_record.room, DangDu=last_record.DangDu, Pattern=last_record.Pattern, Speed=mode,
                        State=last_record.State, StartDate=timezone.now(),feerate=feerate)
    obj.save()
    return 0

def power_off(room_no,time):
    return 0

def create_dlr(self):
    return 0

def create_dlc(self):
    return 0


# 若输入的值为1显示费用，使用时间
# 若输入的值为2显示空调开关次数，打印详单次数
# 若输入的值为3显示温度改变次数，风速改变次数
# 若输入的值为4显示被调度的次数
# 若输入其他值显示该房间的全部信息


def get_daily_record():         #   从json中获取信息
    with open('C:/Users/74546/Desktop/python_try_web/mysite/后台数据.json', 'r', encoding='utf-8') as f:
        daily_data = json.load(f)
    return daily_data


def daily_record_room(request):         #   查看每日全部信息
    t = get_daily_record()
    return render(
        request,
        'daily_record_manager.html',
        {'daily_data': t}
    )


def get_detail_record(room_id, choice):
    t = get_daily_record()
    if choice == 1:
        for i in t:
            if int(i['room_id']) - int(room_id) == 0:
                key_dic_1 = ['total_fee', 'duration']
                value_dic_1 = [i['total_fee'], i['duration']]
                dict1 = dict(zip(key_dic_1, value_dic_1))
                return dict1
        return 1  # 没有该房间号
    elif choice == 2:
        for i in t:
            if int(i['room_id']) - int(room_id) == 0:
                key_dic_2 = ['times_of_on', 'number_of_RDR']
                value_dic_2 = [i['times_of_on'], i['number_of_RDR']]
                dict2 = dict(zip(key_dic_2, value_dic_2))
                return dict2
        return 1  # 没有该房间号
    elif choice == 3:
        for i in t:
            if int(i['room_id']) - int(room_id) == 0:
                key_dic_3 = ['times_of_change_temp', 'times_of_change_speed']
                value_dic_3 = [i['times_of_change_temp'], i['times_of_change_speed']]
                dict3 = dict(zip(key_dic_3, value_dic_3))
                return dict3
        return 1    #没有该房间号
    elif choice == 4:
        for i in t:
            if int(i['room_id']) - int(room_id) == 0:
                key_dic_4 = ['times_of_dispatch']
                value_dic_4 = [i['times_of_dispatch']]
                dict4 = dict(zip(key_dic_4, value_dic_4))
                return dict4
        return 1    #没有该房间号
    else:
        for i in t:
            if int(i['room_id']) - int(room_id) == 0:
                key_dic = ['room_id', 'times_of_on', 'duration', 'total_fee', 'times_of_dispatch', 'number_of_RDR',
                            'times_of_change_temp', 'times_of_change_speed']
                value_dic = [i['room_id'], i['times_of_on'], i['duration'], i['total_fee'], i['times_of_dispatch'],
                            i['number_of_RDR'], i['times_of_change_temp'], i['times_of_change_speed']]
                dictm = dict(zip(key_dic, value_dic))
            return dictm
        return 1  # 没有该房间号


def find_daily_record(request):
    if request.method == "GET":
        return render(request, 'daily_record_room_choice.html')

    else:
        choice_test = request.POST.get('choice')
        # print('********************************************')
        room_id_test = request.POST.get('room_id')
        # print('********************************************')
        choice_test = int(choice_test)
        room_id_test = int(room_id_test)
        t = get_detail_record(room_id_test, choice_test)
        print(t)
        if t == 1:       #房间没找到，返回原来界面
            return render(request, 'daily_record_room_choice.html')
        else:
            if int(choice_test) == 1:
                return render(
                    request,
                    'daily_record_room.html',
                    get_detail_record(room_id_test, choice_test)
                    )
            elif choice_test == 2:
                return render(
                    request,
                    'daily_record_room_1.html',
                    get_detail_record(room_id_test, choice_test)
                )
            elif choice_test == 3:
                return render(
                    request,
                    'daily_record_room_2.html',
                    get_detail_record(room_id_test, choice_test)
                )
            elif choice_test == 4:
                return render(
                    request,
                    'daily_record_room_3.html',
                    get_detail_record(room_id_test, choice_test)
                )
            else:
                return render(
                    request,
                    'daily_record_room_4.html',
                    get_detail_record_weekly(room_id_test, choice_test)
                )



def get_weekly_record():         #   从json中获取信息
    with open('D:/python_try_web/mysite/后台数据.json', 'r', encoding='utf-8') as f:
        weekly_data = json.load(f)
    return weekly_data


def puls_data(room_id):    #往后加7个
    t = get_weekly_record()
    count = 0
    now_id = room_id
    now_on = 0
    now_duration = 0
    now_total_fee = 0
    now_dispatch = 0
    now_RDR = 0
    now_change_temp = 0
    now_change_speed = 0
    key_dic = ['room_id', 'times_of_on', 'duration', 'total_fee', 'times_of_dispatch', 'number_of_RDR', 'times_of_change_temp', 'times_of_change_speed']
    for i in t:
        if int(i['room_id']) == room_id:
            now_on = int(i['times_of_on']) + now_on
            now_duration = int(i['duration']) + now_duration
            now_total_fee = int(i['total_fee']) + now_total_fee
            now_dispatch = int(i['times_of_dispatch']) + now_dispatch
            now_RDR = int(i['number_of_RDR']) + now_RDR
            now_change_temp = int(i['times_of_change_temp']) + now_change_temp
            now_change_speed = int(i['times_of_change_speed']) + now_change_speed
            count = count + 1
            if count == 6:
                break
    value_dic = [now_id, now_on, now_duration, now_total_fee, now_dispatch, now_RDR, now_change_temp, now_change_speed]
    dict1 = dict(zip(key_dic, value_dic))
    return dict1


def get_detail_record_weekly(room_id, choice):
    t = puls_data(room_id)
    if choice == 1:
        if int(t['room_id']) - int(room_id) == 0:
            key_dic_1 = ['total_fee', 'duration']
            value_dic_1 = [t['total_fee'], t['duration']]
            dict1 = dict(zip(key_dic_1, value_dic_1))
            return dict1
        return 1  # 没有该房间号
    elif choice == 2:
        if int(t['room_id']) - int(room_id) == 0:
            key_dic_2 = ['times_of_on', 'number_of_RDR']
            value_dic_2 = [t['times_of_on'], t['number_of_RDR']]
            dict2 = dict(zip(key_dic_2, value_dic_2))
            return dict2
        return 1  # 没有该房间号
    elif choice == 3:
        if int(t['room_id']) - int(room_id) == 0:
            key_dic_3 = ['times_of_change_temp', 'times_of_change_speed']
            value_dic_3 = [t['times_of_change_temp'], t['times_of_change_speed']]
            dict3 = dict(zip(key_dic_3, value_dic_3))
            return dict3
        return 1    #没有该房间号
    elif choice == 4:
        if int(t['room_id']) - int(room_id) == 0:
            key_dic_4 = ['times_of_dispatch']
            value_dic_4 = [t['times_of_dispatch']]
            dict4 = dict(zip(key_dic_4, value_dic_4))
            return dict4
        return 1    #没有该房间号
    else:
        if int(t['room_id']) - int(room_id) == 0:
            key_dic = ['room_id', 'times_of_on', 'duration', 'total_fee', 'times_of_dispatch', 'number_of_RDR',
                       'times_of_change_temp', 'times_of_change_speed']
            value_dic = [t['room_id'], t['times_of_on'], t['duration'], t['total_fee'], t['times_of_dispatch'],
                         t['number_of_RDR'], t['times_of_change_temp'], t['times_of_change_speed']]
            dictm = dict(zip(key_dic, value_dic))
            return dictm
        return 1  # 没有该房间号


def find_weekly_record(request):
    # print(request.method)
    if request.method == "GET":
        # print('aaaaaaaaaaaaaaaa')
        return render(request, 'weekly_record_room_choice.html')

    else:
        choice_test = request.POST.get('choice')
        print('********************************************')
        room_id_test = request.POST.get('room_id')
        print('********************************************')
        choice_test = int(choice_test)
        room_id_test = int(room_id_test)
        t = get_detail_record_weekly(room_id_test, choice_test)

        print(t)
        if t == 1:       #房间没找到，返回原来界面
            return render(request, 'weekly_record_room_choice.html')
        else:
            if int(choice_test) == 1:
                return render(
                    request,
                    'daily_record_room.html',
                    get_detail_record_weekly(room_id_test, choice_test)
                    )
            elif choice_test == 2:
                return render(
                    request,
                    'daily_record_room_1.html',
                    get_detail_record_weekly(room_id_test, choice_test)
                )
            elif choice_test == 3:
                return render(
                    request,
                    'daily_record_room_2.html',
                    get_detail_record_weekly(room_id_test, choice_test)
                )
            elif choice_test == 4:
                return render(
                    request,
                    'daily_record_room_3.html',
                    get_detail_record_weekly(room_id_test, choice_test)
                )
            else:
                return render(
                    request,
                    'weekly_record_manager.html',
                    get_detail_record_weekly(room_id_test, choice_test)
                )
