from django.shortcuts import render
import json


def make_record():
    with open('E:/codes/306c/后台数据.json', 'r', encoding='utf-8') as f:
        weekly_data = json.load(f)
    return weekly_data


def puls_data(room_id):    #往后加7个
    t = make_record()
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



def print_weekly_record(request):
    dic = puls_data(1)
    print(dic)
    return render(
        request,
        'weekly_record_manager.html',
        dic
    )
