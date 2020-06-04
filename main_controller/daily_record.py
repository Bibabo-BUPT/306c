from django.shortcuts import render
import json

def make_record():
    with open('D:/python_try_web/mysite/后台数据.json', 'r', encoding='utf-8') as f:
        daily_data = json.load(f)
    return daily_data


def print_daily_record(request):
    t = make_record()
    return render(
        request,
        'daily_record_manager.html',
        {'daily_data': t}
    )
