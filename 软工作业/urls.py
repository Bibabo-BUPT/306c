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
from main_controller import views

from main_controller import daily_record
from main_controller import room
from main_controller import weekly_record



urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/',views.room),
    path('administrator/',views.administrator),
    path('power_on/',views.power_on_html),
    path('set_default/',views.set_default_html),
    path('login/',views.login),
    path('reception_login/',views.reception_login),
    path('reception_print/',views.reception_print),
    path('reception_check_in/',views.reception_check_in),
    path('reception_check_out/',views.reception_check_out),
    path('reception_print_bill/',views.reception_print_bill),
    path('reception_print_detail/',views.reception_print_detail),
    path(r'daily_record_manager/', daily_record.print_daily_record),
    #path(r'daily_record_manager/', room.daily_record_room),  # 查看全部信息
    path(r'daily_record_room_choice/', room.find_daily_record),  # 选择界面
    path(r'weekly_record_manager/', weekly_record.print_weekly_record),
    path(r'weekly_record_room_choice/', room.find_weekly_record)
]