from django.db import models
import re
# Create your models here.


class FeedbackMotorTest(models.Model):
    Title = models.CharField(max_length=256, null=True, verbose_name="反馈标题")
    Text = models.CharField(max_length=2555, null=True, verbose_name="反馈内容")
    user = models.CharField(max_length=255, null=True, verbose_name="反馈用户")
    isSolved = models.BooleanField(default=False, verbose_name="是否被解决")
    cTime = models.DateTimeField(auto_now_add=True, verbose_name="反馈时间")

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ["cTime"]
        verbose_name = "用户反馈"
        verbose_name_plural = "用户反馈"


class Software(models.Model):
    Title = models.CharField(max_length=256, verbose_name="上位机版本管理")
    cTime = models.DateTimeField(auto_now_add=True, verbose_name="版本上传时间")
    version = models.IntegerField(verbose_name="软件版本")
    isLatest = models.BooleanField(default=False, verbose_name="是否设置为最新版本")
    downloadAddress = models.FileField(upload_to="SoftwareFile", verbose_name="上位机下载地址", default=True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ["-version"]
        verbose_name = "上位机版本管理"
        verbose_name_plural = "上位机版本管理"


class TestResult(models.Model):
    Title = models.CharField(max_length=256, null=True, verbose_name="测试主题")
    testId = models.CharField(max_length=255, unique=True, verbose_name="测试ID", default="0")
    cTime = models.DateTimeField(auto_now_add=True, verbose_name="测试时间")
    isPassed = models.BooleanField(default=False, verbose_name="测试是否通过")
    user = models.CharField(max_length=256, verbose_name="测试人员")
    motorMemory = models.OneToOneField('Memory', on_delete=models.CASCADE, verbose_name="电机内存表", blank=True)
    FunctionResult = models.OneToOneField("Function", on_delete=models.CASCADE, verbose_name="电机功能测试表", blank=True)
    testLog = models.FileField(upload_to="MotorTest/%Y/%m", verbose_name="电机测试记录log", blank=True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ["-cTime"]
        verbose_name = "测试结果"
        verbose_name_plural = "测试结果"


class Function(models.Model):
    testId = models.CharField(max_length=255, unique=True, verbose_name="测试ID", default="0")
    isPaired = models.BooleanField(default=False, verbose_name="配对功能")
    isType = models.BooleanField(default=False, verbose_name="设备类型是否匹配")
    setLimit = models.BooleanField(default=False, blank=True, verbose_name="设置行程")
    percentControl = models.BooleanField(default=False, blank=True, verbose_name="百分比控制")
    angleControl = models.BooleanField(default=False, blank=True, verbose_name="角度控制")
    upControl = models.BooleanField(default=False, blank=True, verbose_name="上行功能")
    downControl = models.BooleanField(default=False, blank=True, verbose_name="下行功能")
    upJogControl = models.BooleanField(default=False, blank=True, verbose_name="上点动功能")
    downJogControl = models.BooleanField(default=False, blank=True, verbose_name="下点动功能")
    setThirdLimit = models.BooleanField(default=False, blank=True, verbose_name="设置第三行程")
    delThirdLimit = models.BooleanField(default=False, blank=True, verbose_name="删除第三行程")
    delLimit = models.BooleanField(default=False, blank=True, verbose_name="删除行程")
    isChangeState = models.BooleanField(default=False, blank=True, verbose_name="状态实时变化功能")
    cTime = models.DateTimeField(auto_now_add=True, verbose_name="功能测试时间")

    def __str__(self):
        return "功能测试表"+str(self.cTime)

    class Meta:
        ordering = ["-cTime"]
        verbose_name = "功能测试表"
        verbose_name_plural = "功能测试表"


class Memory(models.Model):
    testId = models.CharField(max_length=255, unique=True, verbose_name="测试ID", default="0")
    moduleVersion = models.CharField(max_length=256, verbose_name="模块版本")
    motorState = models.CharField(max_length=256, verbose_name="电机状态")
    motorPosition = models.CharField(max_length=256, verbose_name="当前位置")
    angleLevel = models.CharField(max_length=256, verbose_name="角度系数")
    currentSpeed = models.CharField(max_length=256, verbose_name="当前转速")
    currentVoltage = models.FloatField(blank=True, verbose_name="当前电压")
    speedLevel = models.IntegerField(blank=True, verbose_name="当前速度等级")
    jogLength = models.IntegerField(blank=True, verbose_name="点动距离系数")
    thirdLimitPosition = models.CharField(max_length=256, blank=True, verbose_name="第三行程点位置")
    sceneSum = models.CharField(max_length=256, verbose_name="场景校验和")
    voltagePercent = models.IntegerField(verbose_name="电量百分比")
    deviceType = models.CharField(max_length=256, verbose_name="设备类型")
    deviceName = models.CharField(max_length=256, verbose_name="设备名字")
    deviceSoftwareVersion = models.FloatField(verbose_name="设备软件版本")
    workVoltage = models.FloatField(verbose_name="工作电压")
    deviceLoad = models.FloatField(verbose_name="电机负载")
    motorSpeed = models.IntegerField(verbose_name="电机速度")
    motorLimitState = models.CharField(max_length=256, verbose_name="电机行程状态")

    def __str__(self):
        return "电机内存表"

    class Meta:
        verbose_name = "电机内存表"
        verbose_name_plural = "电机内存表"







