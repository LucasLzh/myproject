from django.contrib import admin
from .models import  *
# Register your models here.


class SoftWAREAdmin(admin.ModelAdmin):
    list_display = ('Title', 'cTime', 'version', 'isLatest', 'downloadAddress')


class TestResultAdmin(admin.ModelAdmin):
    list_display = ('Title', 'cTime', 'isPassed', 'user', 'motorMemory', 'FunctionResult', 'testLog')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Text', 'user', 'isSolved', 'cTime')


admin.site.register(FeedbackMotorTest, FeedbackAdmin)
admin.site.register(TestResult, TestResultAdmin)
admin.site.register(Function)
admin.site.register(Memory)
admin.site.register(Software, SoftWAREAdmin)