from django.db import models
import re

# Create your models here.


class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=256, default="")
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    cTime = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-cTime"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ConfirmString(models.Model):
    """
    用来保证用户和注册码之间关系的唯一性
    """
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE, )
    cTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:
        ordering = ['-cTime']
        verbose_name = "确认码"
        verbose_name_plural = "确认码"


"""
电机的产品模块
"""


class Voltage(models.Model):
    voltage = models.IntegerField(unique=True, verbose_name="工作电压")

    def __str__(self):
        return str(self.voltage)

    class Meta:
        verbose_name = "工作电压"
        verbose_name_plural = verbose_name


class RatedTorque(models.Model):
    torque = models.CharField(max_length=32, unique=True, verbose_name="额定扭矩")

    def __str__(self):
        return self.torque

    class Meta:
        verbose_name = "额定扭矩"
        verbose_name_plural = verbose_name


class RatedSpeed(models.Model):
    speed = models.CharField(max_length=32, unique=True, verbose_name="额定转速Rpm")

    def __str__(self):
        return self.speed

    class Meta:
        verbose_name = "额定转速"
        verbose_name_plural = verbose_name


class RatedCurrent(models.Model):
    current = models.CharField(max_length=32, unique=True, verbose_name="额定电流A")

    def __str__(self):
        return self.current

    class Meta:
        verbose_name = "额定电流"
        verbose_name_plural = verbose_name


class RatedPower(models.Model):
    power = models.CharField(max_length=32, unique=True, verbose_name="额定功率W")

    def __str__(self):
        return self.power

    class Meta:
        verbose_name = "额定功率"
        verbose_name_plural = verbose_name


class DegreeOfProtection(models.Model):
    protection = models.CharField(max_length=32, unique=True, verbose_name="防护等级IP")

    def __str__(self):
        return self.protection

    class Meta:
        verbose_name = "防护等级"
        verbose_name_plural = verbose_name


class MotorImg(models.Model):
    # power = models.ForeignKey("RatedPower", on_delete=models.CASCADE, default=True)
    img1 = models.ImageField(upload_to="image/%Y/%m/%d", verbose_name="电机图片1", default=True)
    img2 = models.ImageField(upload_to="image/%Y/%m/%d", verbose_name="电机图片2", default=True)
    img3 = models.ImageField(upload_to="image/%Y/%m/%d", verbose_name="电机图片3", default=True)

    def __str__(self):
        a = re.split('[/ ]', str(self.img1.name))
        return a[-1]

    class Meta:
        verbose_name = "电机测试图片"
        verbose_name_plural = verbose_name


class Label(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="标签名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签名"
        verbose_name_plural = verbose_name


class Motor(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="电机名称")
    # img = models.ImageField(upload_to="static/Motor",
    #                         default=u"static/Motor/default.img",
    #                         max_length=100,
    #                         verbose_name="电机图片")
    img = models.ForeignKey("MotorImg", on_delete=models.CASCADE, default=True, verbose_name="电机图片一对多")
    # img = models.ImageField(upload_to="static/Motor/", verbose_name="电机图片")
    torque = models.ForeignKey("RatedTorque", on_delete=models.CASCADE)
    voltage = models.ForeignKey("Voltage", on_delete=models.CASCADE, null=True)
    speed = models.ForeignKey("RatedSpeed", on_delete=models.CASCADE)
    current = models.ForeignKey("RatedCurrent", on_delete=models.CASCADE)
    protection = models.ForeignKey("DegreeOfProtection", on_delete=models.CASCADE)
    label = models.ManyToManyField('Label')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "电机名称"
        verbose_name_plural = verbose_name



"""
下面是测试用的模块
"""


# class Menu(models.Model):
#     """
#     菜单
#     """
#     title = models.CharField(max_length=32, unique=True, verbose_name=u"菜单")
#     icon = models.CharField(max_length=32, verbose_name=u"菜单图标", null=True, blank=True)
#     parent = models.ForeignKey("Menu", null=True, blank=TypeError, on_delete=models.CASCADE)
#
#     def __str__(self):
#         title_list = [self.title]
#         p = self.parent
#         while p:
#             title_list.insert(0, p.title)
#             p = p.parent
#         return '-'.join(title_list)
#
#     class Meta:
#         verbose_name = u"菜单"
#         verbose_name_plural = verbose_name
#
#
# class Permission(models.Model):
#     """
#     权限
#     """
#     title = models.CharField(max_length=32, unique=True, verbose_name=u"权限")
#     url = models.CharField(max_length=128, unique=True)
#     icon = models.CharField(max_length=32, verbose_name=u"权限图标", null=True, blank=True)
#     menu = models.ForeignKey("Menu", null=True, blank=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         #用来显示菜单前缀的权限
#         return '{munu}---{permission}'.format(menu=self.menu, permission=self.title)
#
#     class Meta:
#         verbose_name = u"权限"
#         verbose_name_plural = verbose_name
#
#
# class Role(models.Model):
#     """
#     角色：绑定权限
#     """
#     title = models.CharField(max_length=32, unique=True, verbose_name=u"角色")
#     permissions = models.ManyToManyField("Permission")
#     #角色和权限多对多关系
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = u"角色"
#         verbose_name_plural = verbose_name
#
#
# class UserInfo(models.Model):
#     """
#     用户：划分角色
#     """
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=64)
#     real_name = models.CharField(max_length=50, verbose_name=u"真实姓名", default="")
#     mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机号")
#     image = models.ImageField(upload_to="img/", default=u"img/default.img", max_length=100, verbose_name=u"头像")
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         verbose_name = u"用户"
#         verbose_name_plural = verbose_name
