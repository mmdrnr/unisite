from django.db import models

class study(models.Model):
    study_title = models.CharField(max_length = 250 ,verbose_name ="نام درس")
    study_reshte = models.CharField(max_length =500 ,verbose_name = "رشته")
    study_unit = models.IntegerField( verbose_name="واحد")
    study_code = models.IntegerField(verbose_name="کد درس")
    study_group = models.IntegerField( verbose_name="گروه درس") 
    study_master = models.CharField(max_length=255 , verbose_name="استاد")
    study_capacity = models.IntegerField(verbose_name="ظرفیت")
    # def __str__(self):
    #     return self.study_title
    
