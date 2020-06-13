"""软工作业 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from air_condition_system import views

from air_condition_system import daily_record
from air_condition_system import room
from air_condition_system import weekly_record

from django.conf.urls import url




urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/',views.room),

    #空调管理员
    path('login/',views.login),
    path('administrator/power_on/',views.power_on),
    path('administrator/set_parameter/',views.set_parameter),
    path('administrator/start_up/',views.start_up),
    path('administrator/check_room_state',views.check_room_state),
    path('administrator/power_off/',views.power_off),

    #前台
    #path('reception_login/',views.reception_login),
    #path('reception_print/',views.reception_print),
    path('reception/check_in/',views.check_in),
    path('reception/check_out/',views.check_out),
    path('reception/check_bill/',views.check_bill),
    path('reception/check_RDR/',views.check_RDR),

    #经理
    path(r'daily_record_manager/', daily_record.print_daily_record),
    path(r'daily_record_room_choice/', room.find_daily_record),  # 选择界面
    path(r'weekly_record_manager/', weekly_record.print_weekly_record),
    path(r'weekly_record_room_choice/', room.find_weekly_record),

    #url('Record/',views.Record,name="Record"),#记录表
    #url('User/',views.User,name="User"),#用户
    #url('Money/',views.Money,name="Money"),#查询金额
    #url('State/',views.State,name="State"),#修改开机状态
   # url('modea/',views.modea,name="modea"),#下调温度
    #url('Speed/',views.Speed,name="Speed"),#调风速
    #url('modeName/',views.modeName,name="modeName"),#调模式
   # url('MoneyA/',views.MoneyA,name="MoneyA"),#写入金额
    url('customer/power_on/',views.customer_power_on),#用户开机
    url('customer/power_off/',views.customer_power_off),
    url('customer/room_request/',views.room_request),
    url('customer/change_target_temp/',views.change_target_temp),
    url('customer/change_target_speed/',views.change_target_speed),
    url('customer/get_temp_cost/',views.loop),

]
