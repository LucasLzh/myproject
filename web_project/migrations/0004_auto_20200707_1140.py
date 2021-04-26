# Generated by Django 3.0.6 on 2020-07-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_project', '0003_auto_20200707_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签名',
                'verbose_name_plural': '标签名',
            },
        ),
        migrations.AddField(
            model_name='motor',
            name='label',
            field=models.ManyToManyField(to='web_project.Label'),
        ),
    ]
