from django.db import models
import datetime

# Create your models here.
###########################################
class user_info(models.Model):
    ID = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_key = models.CharField(max_length=30)
    v_id = models.IntegerField(max_length=20)
#########################################
class md_doc(models.Model):
    ID = models.AutoField(primary_key=True)
    val_id = models.IntegerField(max_length=20)
    md_name = models.CharField(max_length=30)
    md_type = models.IntegerField(max_length=20)
    md_key = models.IntegerField(max_length=60000)
    md_web = models.CharField(max_length=100)
#########################################
class md0001(models.Model):
    ID = models.AutoField(primary_key=True)
    md_id = models.ForeignKey(to="md_doc", to_field="ID", on_delete=models.CASCADE)
    dvc_ID = models.IntegerField(max_length=100)
    Tmark = models.IntegerField(max_length=100)
    Vin = models.IntegerField(max_length=30)
    Iin = models.IntegerField(max_length=30)
    Iout = models.IntegerField(max_length=30)
#########################################
class md0001c1(models.Model):
    ID = models.AutoField(primary_key=True)
    md_id = models.ForeignKey(to="md_doc", to_field="ID", on_delete=models.CASCADE)
    dvc_ID = models.IntegerField(max_length=100)
    Tmark = models.IntegerField(max_length=100)
    Vin = models.IntegerField(max_length=30)
    Iin = models.IntegerField(max_length=30)
    Iout = models.IntegerField(max_length=30)
#########################################
class md0002(models.Model):
    ID = models.AutoField(primary_key=True)
    md_id = models.ForeignKey(to="md_doc", to_field="ID", on_delete=models.CASCADE)
    dvc_ID = models.IntegerField(max_length=100)
    Tmark = models.IntegerField(max_length=100)
    Vin = models.IntegerField(max_length=30)
    Iin = models.IntegerField(max_length=30)
    Tin = models.IntegerField(max_length=30)
    Tout = models.IntegerField(max_length=30)
    Flow = models.IntegerField(max_length=30)
#########################################
class md0003(models.Model):
    ID = models.AutoField(primary_key=True)
    md_id = models.ForeignKey(to="md_doc", to_field="ID", on_delete=models.CASCADE)
    dvc_ID = models.IntegerField(max_length=100)
    Tmark = models.IntegerField(max_length=100)
    Vin = models.IntegerField(max_length=30)
    Iin = models.IntegerField(max_length=30)
    Tcin = models.IntegerField(max_length=30)
    Tcout = models.IntegerField(max_length=30)
    Tein = models.IntegerField(max_length=30)
    Teout = models.IntegerField(max_length=30)
    Eflow = models.IntegerField(max_length=30)
#########################################
class md0004(models.Model):
    ID = models.AutoField(primary_key=True)
    md_id = models.ForeignKey(to="md_doc", to_field="ID", on_delete=models.CASCADE)
    dvc_ID = models.IntegerField(max_length=100)
    Tmark = models.IntegerField(max_length=100)
    city = models.IntegerField(max_length=30)
    age = models.IntegerField(max_length=30)
    sexual = models.IntegerField(max_length=30)
    getuptime = models.IntegerField(max_length=30)
    sleeptime = models.IntegerField(max_length=30)
    readtime = models.IntegerField(max_length=30)
    sporttime = models.IntegerField(max_length=30)
    phonetime = models.IntegerField(max_length=30)
    roadtime = models.IntegerField(max_length=30)
    familytime = models.IntegerField(max_length=30)
    dreamtime = models.IntegerField(max_length=30)
#########################################
class md0005(models.Model):
    ID = models.AutoField(primary_key=True)
    md_id = models.ForeignKey(to="md_doc", to_field="ID", on_delete=models.CASCADE)
    dvc_ID = models.IntegerField(max_length=100)
    Tmark = models.IntegerField(max_length=100)
    pwe = models.IntegerField(max_length=30)
    rou = models.IntegerField(max_length=30)
    fspeed = models.IntegerField(max_length=30)
    farea = models.IntegerField(max_length=30)
    pin = models.IntegerField(max_length=30)
    pout = models.IntegerField(max_length=30)

#########################################
class md0006(models.Model):
    ID = models.AutoField(primary_key=True)
    md_id = models.ForeignKey(to="md_doc", to_field="ID", on_delete=models.CASCADE)
    dvc_ID = models.IntegerField(max_length=100)
    Tmark = models.IntegerField(max_length=100)
    pstc = models.IntegerField(max_length=30)
    gstc = models.IntegerField(max_length=30)
    tstc = models.IntegerField(max_length=30)
    gt = models.IntegerField(max_length=30)
    vw = models.IntegerField(max_length=30)
    tair = models.IntegerField(max_length=30)

#########################################
class md0007(models.Model):
    ID = models.AutoField(primary_key=True)
    md_id = models.ForeignKey(to="md_doc", to_field="ID", on_delete=models.CASCADE)
    dvc_ID = models.IntegerField(max_length=100)
    Tmark = models.IntegerField(max_length=100)
    ho = models.IntegerField(max_length=30)
    heqp = models.IntegerField(max_length=30)
    npp = models.IntegerField(max_length=30)
    froof = models.IntegerField(max_length=30)
    fwall = models.IntegerField(max_length=30)
    treal = models.IntegerField(max_length=30)
    taim = models.IntegerField(max_length=30)
    vair = models.IntegerField(max_length=30)

#########################################