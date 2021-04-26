from django.contrib import admin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'email', 'password', 'cTime')
    list_filter = ['sex', 'name', 'cTime']
    search_fields = ['sex', 'name', 'cTime']


class ConfirmAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'cTime')


class MotorAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'voltage', 'torque', 'speed', 'current', 'protection', '电机标签')

    def 电机标签(self, obj):
        return [bt.name for bt in obj.label.all()]

    filter_horizontal = ('label',)


class Img(admin.ModelAdmin):
    list_display = ('img1', 'img2', 'img3')


admin.site.register(User, UserAdmin)
admin.site.register(ConfirmString, ConfirmAdmin)

admin.AdminSite.site_header = '杜亚后台管理系统'
admin.AdminSite.site_title = 'Dooya'

admin.site.register(Voltage)
admin.site.register(RatedTorque)
admin.site.register(RatedSpeed)
admin.site.register(RatedCurrent)
admin.site.register(RatedPower)
admin.site.register(DegreeOfProtection)

admin.site.register(Motor, MotorAdmin)

admin.site.register(MotorImg, Img)
admin.site.register(Label)

