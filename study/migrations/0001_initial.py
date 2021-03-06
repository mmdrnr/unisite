# Generated by Django 3.0.6 on 2020-06-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_title', models.CharField(max_length=250, verbose_name='نام درس')),
                ('study_reshte', models.CharField(max_length=500, verbose_name='رشته')),
                ('study_unit', models.IntegerField(max_length=1, verbose_name='واحد')),
                ('study_code', models.IntegerField(max_length=255, verbose_name='کد درس')),
                ('study_group', models.IntegerField(max_length=255, verbose_name='گروه درس')),
                ('study_master', models.CharField(max_length=255, verbose_name='استاد')),
                ('study_capacity', models.IntegerField(max_length=2, verbose_name='ظرفیت')),
            ],
        ),
    ]
