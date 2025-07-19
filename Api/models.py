from django.db import models

class Builder(models.Model):
    builder_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class AircraftCarrierClass(models.Model):
    class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    displacement = models.IntegerField()
    length = models.IntegerField()
    beam = models.IntegerField()
    aircrafts = models.IntegerField()
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE, related_name='classes')

class AircraftCarrier(models.Model):
    ac_id = models.AutoField(primary_key=True)
    hull_number = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    vessel_class = models.ForeignKey(AircraftCarrierClass, on_delete=models.CASCADE, related_name='vessels')

class Armament(models.Model):
    arm_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    arm_type = models.CharField(max_length=25)

class ACClassArmament(models.Model):
    aa_id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(AircraftCarrierClass, on_delete=models.CASCADE, related_name='armament')
    quantity = models.IntegerField()
    arm_id = models.ForeignKey(Armament, on_delete=models.CASCADE)