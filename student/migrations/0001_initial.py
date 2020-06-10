# Generated by Django 3.0.6 on 2020-06-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255, verbose_name='نام')),
                ('student_family', models.CharField(max_length=350, verbose_name='نام خانوادگی')),
                ('student_id', models.CharField(max_length=255, verbose_name='شماره دانشجویی')),
                ('meli_code', models.CharField(max_length=255, verbose_name='کد ملی')),
                ('father_name', models.CharField(max_length=255, verbose_name='نام پدر')),
                ('student_phone', models.CharField(max_length=255, verbose_name='شماره همراه ')),
                ('father_phone', models.CharField(max_length=255, verbose_name='شماره همراه پدر')),
                ('mother_phone', models.CharField(max_length=255, verbose_name='شماره همراه مادر')),
                ('home_phone', models.CharField(max_length=255, verbose_name='شماره منزل')),
                ('mazhab', models.CharField(max_length=255, verbose_name='مذهب')),
                ('birthyear', models.IntegerField(max_length=4, verbose_name='سال تولد')),
                ('birthmonth', models.IntegerField(max_length=2, verbose_name='ماه تولد')),
                ('birthdany', models.IntegerField(max_length=2, verbose_name='روز تولد')),
                ('enter_year', models.IntegerField(max_length=4, verbose_name='سال ورود')),
                ('reshte', models.CharField(max_length=300, verbose_name='رشته تحصیلی')),
                ('maghta_tahsil', models.CharField(max_length=255, verbose_name='مقطع تحصیلی')),
                ('uni_name', models.CharField(max_length=255, verbose_name='نام دانشگاه')),
                ('daneshkade_name', models.CharField(max_length=255, verbose_name='نام دانشکده')),
                ('bank_id', models.CharField(max_length=255, verbose_name='شماره کارت بانکی')),
                ('address', models.TextField(verbose_name='آدرس محل سکونت')),
                ('pasword', models.CharField(max_length=255, verbose_name='رمز عبور')),
            ],
        ),
    ]
