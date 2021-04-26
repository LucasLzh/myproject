# Generated by Django 3.0.6 on 2020-07-07 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_project', '0002_auto_20200707_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motorimg',
            name='power',
        ),
        migrations.AddField(
            model_name='motorimg',
            name='img1',
            field=models.ImageField(default=True, upload_to='static/Motor/', verbose_name='电机图片1'),
        ),
        migrations.AddField(
            model_name='motorimg',
            name='img2',
            field=models.ImageField(default=True, upload_to='static/Motor/', verbose_name='电机图片2'),
        ),
        migrations.AddField(
            model_name='motorimg',
            name='img3',
            field=models.ImageField(default=True, upload_to='static/Motor/', verbose_name='电机图片3'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='img',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='web_project.MotorImg', verbose_name='电机图片一对多'),
        ),
    ]
