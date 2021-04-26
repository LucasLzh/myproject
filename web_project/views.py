import os
from django.http import FileResponse
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from Dooya_web import forms
from web_project import models
import hashlib, datetime
from Dooya_web import settings
import logging
import json
import time
from django.core.paginator import Paginator
# Create your views here.

logger = logging.getLogger(__name__)


def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user,)
    return code


def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives

    subject = 'Dooya web账号注册系统'

    text_content = '''感谢注册Dooya web！\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！
                    或者复制下面的网站链接地址到服务器：
                    http://{}/confirm/?code={}" target=blank
                    '''.format('127.0.0.1:8080', code)

    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>Dooya web测试系统</a></p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8080', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def main_page(request):
    # obj = models.Motor.objects.get(name="DM15M-20/15")
    # error_happens = True
    # if error_happens:
    #     # Log an error message
    #     logger.error('Something went wrong!')
    #     logger.warning("this is warning!")
    return render(request, 'DooyaWeb/index.html', locals())


def auto_sys(request):
    return render(request, 'DooyaWeb/auto_sys.html', locals())


def solutions(request):
    if request.method == "POST":
        voltage = request.POST['voltage']
        v = int(voltage)
        obj = models.Motor.objects.filter(voltage__voltage=v).values('name', 'voltage__voltage', 'img__img1')
        obj = list(obj)
        list_data = {
            "status": True,
            'data': obj
        }
        # a = json.dumps(obj)
        print(list_data)
        return JsonResponse(list_data)
    else:
        try:
            obj = models.Motor.objects.all()
        except:
            print("数据获取异常")
            pass

    return render(request, 'DooyaWeb/solutions.html', locals())

def product(request):
    return render(request, 'DooyaWeb/product.html', locals())



def register(request):
    print("已经进入到注册页面")
    if request.method == "GET":
        registerForm = forms.RegisterForm()
        return render(request, 'test/Register.html', locals())
    else:
        registerForm = forms.RegisterForm(request.POST)
        message = "请注意填写的内容分"
        if registerForm.is_valid():
            username = models.User.objects.filter(name=registerForm.cleaned_data['username'])
            email = models.User.objects.filter(email=registerForm.cleaned_data['email'])
            if username:
                message = "该用户名已存在"
                return render(request, 'test/Register.html', locals())
            if email:
                message = "该邮箱已被注册"
                return render(request, "test/Register.html", locals())
            if registerForm.cleaned_data['password1'] != registerForm.cleaned_data['password2']:
                message = "两次的密码不同"
                return render(request, 'test/Register.html', locals())
            new_user = models.User()
            new_user.name = registerForm.cleaned_data['username']
            new_user.password = hash_code(registerForm.cleaned_data['password1'])
            new_user.email = registerForm.cleaned_data['email']
            print(new_user.password)
            new_user.gender = registerForm.cleaned_data['sex']
            new_user.save()
            code = make_confirm_string(new_user)
            send_email(registerForm.cleaned_data['email'], code)
        else:
            print("不符合要求")
            message = "不符合要求"
            return render(request, 'test/Register.html', locals())
        return render(request, "test/MainPage.html", locals())


def confirm_user(request):
    code = request.GET.get('code', None)
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = "这是一个无效的链接请求"
        return render(request, "test/MainPage.html", locals())
    c_time = confirm.cTime
    now_time = datetime.datetime.utcnow()
    if now_time > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        message = "超过请求的有效期，请重新激活"
        return render(request, 'test/MainPage.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = "确认成功，可以正常点登录"
        return render(request, 'test/MainPage.html', locals())


def sign_out(request):
    request.session.clear()
    return redirect("/")


def log_in(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                u = models.User.objects.get(name=user)
                if not u.has_confirmed:
                    message = "改用户还未确认邮箱，请确认后重新登录！"
                    return render(request, "test/LogIn.html", locals())
                if u.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = u.id
                    request.session['user_name'] = u.name
                    return render(request, "test/MainPage.html", locals())
                else:
                    message = "密码错误，请重新输入！"
                    return render(request, "test/LogIn.html", locals())
            except:
                message = "账号不存在"
            return render(request, "test/LogIn.html", locals())
        else:
            message = "账号或密码错误请重新输入！"
            return render(request, 'test/LogIn.html', locals())
    else:
        login_form = forms.UserForm()
        return render(request, 'test/LogIn.html', locals())


def download(request):
    if request.session['is_login']:
        fileName = request.GET.get('fileName')
        print(fileName)
        file = open('static/files/'+fileName, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename='+fileName
        return response
    else:
        return redirect('/log_in')


def download_testMotor(request):
    fileName_testMotor = request.GET.get('fileName')
    print(fileName_testMotor)
    file = open('static/files/' + fileName_testMotor, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=' + fileName_testMotor
    return response


def request_testMotor_version(request):
    return HttpResponse("3")


def uploadFile(request):
    if request.method == "POST":
        print("进入了post")
        myFile = request.FILES.get("myfile", None)
        # print(myFile.name)
        if not myFile:
            print("文件为空")
            return HttpResponse("上传文件为空")
        openMyFile = open((os.getcwd() + "\static\saveFile\\" + myFile.name), 'wb+')
        for item in myFile.chunks():
            print("开始写入")
            openMyFile.write(item)
            print(item)
        openMyFile.close()
        return HttpResponse("写入完成")
    else:
        print("进入了get")
        return redirect('/')


def uploadFile_winform(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        print("开始接收数据")
        print(data)
        return HttpResponse("写入完成")
    else:
        print("进入了get")
        return redirect('/')


def feedback_motorTest(request):
    if request.method == "POST":
        name = request.POST.get('name')
        topic = request.POST.get('topic')
        content = request.POST.get('content')
        filename = topic + "(" + name + ")"
        openMyFile = open((os.getcwd() + "\static\\feedback_file\\" + filename), 'wb+')
        openMyFile.write(content.encode('utf-8'))
        return HttpResponse("反馈成功")


def page(request):
    print("进入分页功能测试模块")
    pindex = request.GET.get('page', 1)
    a = models.Motor.objects.all()
    page_list = []

    for item in a:
        page_list.append(item)
    print("pagelist:"+ str(page_list))
    data = Paginator(page_list, 20)
    if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
        pindex = 1
    page = data.page(pindex)
    context = {"message": "lucas", "page": page}
    print(str(context))
    return render(request, "test/page.html", context)


