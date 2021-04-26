from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="密码", max_length=256)
    captcha = CaptchaField(label="验证码")


class RegisterForm(forms.Form):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    username = forms.CharField(label="用户名", max_length=128)
    password1 = forms.CharField(label="密码", max_length=256)
    password2 = forms.CharField(label="确认密码", max_length=256)
    email = forms.EmailField(label="邮箱地址", max_length=256)
    sex = forms.ChoiceField(label="性别", choices=gender)
    captcha = CaptchaField(label="验证码", error_messages={'invalid': '验证码不对'})
