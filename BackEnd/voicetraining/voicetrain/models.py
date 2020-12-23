from django.db import models

# Create your models here.
class VoiceTrain(models.Model):
    user = models.CharField(max_length=30)
    voice = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class Deliveryinfo(models.Model):
    username = models.CharField(db_column='userName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shopname = models.CharField(db_column='shopName', max_length=50)  # Field name made lowercase.
    fromaddress = models.CharField(db_column='fromAddress', max_length=50)  # Field name made lowercase.
    destination = models.CharField(max_length=50)
    deliverytime = models.FloatField(db_column='deliveryTime', blank=True, null=True)  # Field name made lowercase.
    alertcount = models.IntegerField(db_column='alertCount', blank=True, null=True)  # Field name made lowercase.
    fromlatitude = models.FloatField(db_column='fromLatitude')  # Field name made lowercase.
    fromlongitude = models.FloatField(db_column='fromLongitude')  # Field name made lowercase.
    deslatitude = models.FloatField(db_column='desLatitude')  # Field name made lowercase.
    deslongitude = models.FloatField(db_column='desLongitude')  # Field name made lowercase.
    assigndate = models.DateField(db_column='assignDate')  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    receipt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DeliveryInfo'



class Deliverysensordata(models.Model):
    id = models.IntegerField(primary_key=True)
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    ay = models.FloatField(db_column='AY', blank=True, null=True)  # Field name made lowercase.
    az = models.FloatField(db_column='AZ', blank=True, null=True)  # Field name made lowercase.
    ax_compare = models.FloatField(db_column='AX_compare', blank=True, null=True)  # Field name made lowercase.
    ay_compare = models.FloatField(db_column='AY_compare', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeliverySensorData'


class Userinfo(models.Model):
    username = models.CharField(max_length=50)
    deliverystatus = models.IntegerField(db_column='deliveryStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserInfo'

