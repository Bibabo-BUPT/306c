from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Record)
admin.site.register(models.User)
admin.site.register(models.Money)

class  UserAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Room')
    search_fields = ('Name')
    list_editable = ('id')
    list_per_page = 10

class RecordAdmin(admin.ModelAdmin):
    list_display = ('DeDu', 'DangDu', 'Pattern','Speed','State')
    search_fields = ('DeDu')
    list_editable = ('id')
    list_per_page = 10

class  MoneyAdmin(admin.ModelAdmin):
    list_display = ('Dmoney', 'Lmoney')
    search_fields = ('Dmoney')
    list_editable = ('Name')
    list_per_page = 10