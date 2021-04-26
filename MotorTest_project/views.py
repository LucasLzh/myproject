import os
from django.http import HttpResponse
from django.shortcuts import render
from MotorTest_project import models
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from Dooya_web import settings
# Create your views here.

emailList = ['lucas.liang@dooya.com', '1030885595@qq.com']


def send_email(email, testUser, motorName):
    from django.core.mail import EmailMultiAlternatives

    subject = '电机测试系统'

    text_content = '''欢迎来到电机测试系统！\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系小梁！
                    '''

    html_content = '''
                    <p>欢迎来到电机测试系统</p>
                    <p>发现测试的电机有问题，测试人员是：{}</p>
                    <p>测试的电机型号是：{}</p>
                    <p>详细的信息可以到后台查看</p>
                    '''.format(testUser, motorName)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@csrf_exempt
def feedback(request):
    if request.method == "POST":
        print(request)
        title = request.POST['title']
        text = request.POST['text']
        user = request.POST['user']
        print(title, text, user)
        obj = models.FeedbackMotorTest(Title=title, Text=text, user=user, isSolved=False)
        obj.save()
        print("保存成功")
        return HttpResponse("success")
    return HttpResponse("failure")


def getVersion(request):
    if request.method == "GET":
        newVersion = models.Software.objects.filter(isLatest=True).first()
        if newVersion:
            a = {'version': str(newVersion.version), "downloadAddress": str(newVersion.downloadAddress)}
        else:
            a = {'version': 0, "downloadAddress": "failed"}
        print(a)
    return HttpResponse(json.dumps(a))


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1", "成功")


def sendTestResult(request):
    if request.method == "POST":
        msgType = request.POST['type']
        if msgType == "testResult":
            testId = request.POST["testId"]
            Title = request.POST["Title"]
            isPassed = request.POST["isPassed"]
            user = request.POST["user"]
            memory = json.loads(request.POST['memory'])
            function = json.loads(request.POST["function"])
            print("-------------------------")
            memory_obj = models.Memory(
                testId=memory['testId'],
                moduleVersion=memory['moduleVersion'],
                motorState=memory['motorState'],
                motorPosition=memory['motorPosition'],
                angleLevel=memory['angleLevel'],
                currentSpeed=memory['currentSpeed'],
                currentVoltage=float(memory['currentVoltage']),
                speedLevel=int(memory['speedLevel']),
                jogLength=int(memory['jogLength']),
                thirdLimitPosition=memory['thirdLimitPosition'],
                sceneSum=memory['sceneSum'],
                voltagePercent=int(memory['voltagePercent']),
                deviceType=memory['deviceType'],
                deviceName=memory['deviceName'],
                deviceSoftwareVersion=float(memory['deviceSoftwareVersion']),
                workVoltage=float(memory['workVoltage']),
                deviceLoad=float(memory['deviceLoad']),
                motorSpeed=int(memory['motorSpeed']),
                motorLimitState=memory['motorLimitState'],
            )
            memory_obj.save()
            function_obj = models.Function(
                testId=function['testId'],
                isPaired=str2bool(function['isPaired']),
                isType=str2bool(function['isType']),
                setLimit=str2bool(function['setLimit']),
                percentControl=str2bool(function['percentControl']),
                angleControl=str2bool(function['angleControl']),
                upControl=str2bool(function['upControl']),
                downControl=str2bool(function['downControl']),
                upJogControl=str2bool(function['upJogControl']),
                downJogControl=str2bool(function['downJogControl']),
                setThirdLimit=str2bool(function['setThirdLimit']),
                delThirdLimit=str2bool(function['delThirdLimit']),
                delLimit=str2bool(function['delLimit']),
                isChangeState=str2bool(function['isChangeState']),
            )
            function_obj.save()
            obj = models.TestResult(
                testId=testId,
                Title=Title,
                isPassed=str2bool(isPassed),
                user=user,
                FunctionResult=models.Function.objects.filter(testId=testId).first(),
                motorMemory=models.Memory.objects.filter(testId=testId).first(),
            )
            obj.save()
            if 1-str2bool(isPassed):
                for email in emailList:
                    print("发送邮件")
                    send_email(email, user, memory['deviceName'])
            pass
        elif msgType == "uploadLog":
            testId = request.POST['testId']
            myFile = request.FILES.get("myfile", None)
            # print(myFile.name)
            if not myFile:
                print("文件为空")
                return HttpResponse("上传文件为空")
            # fileAddress = os.getcwd() + "\\media\\MotorTest\\" + testId + myFile.name
            fileAddress = os.getcwd()+"\\media\\MotorTest" + "\\" + year + "\\0" + month + "\\" + testId + myFile.name
            print("开始上传文件："+fileAddress)
            openMyFile = open(fileAddress, 'wb+')
            for item in myFile.chunks():
                print("开始写入")
                openMyFile.write(item)
                print(item)
            print("写入完成")
            openMyFile.close()
            print("关闭写入")
            models.TestResult.objects.filter(testId=testId).save(testLog=fileAddress)
            return HttpResponse("写入完成")
            pass
        else:
            print("没找到正确的type值")
            pass
        return HttpResponse("success")
    return HttpResponse("use post method")
