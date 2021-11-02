from django.db import models

# Custom User Create
from django.contrib.auth.models import AbstractUser, User

# Random Health Card Generate
from random import randint

# For Add Prescription
import jsonfield


class CustomUser(AbstractUser):
    userImg = models.FileField()
    amount = models.IntegerField()
    fieldName = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=13)
    dob = models.DateField(null=True)
    bloodGroup = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    status = models.CharField(max_length=50)
    token = models.CharField(max_length=150)
    healthCard = models.BooleanField()
    healthCardAcceptByAdmin = models.BooleanField()

    class meta:
        ordering = ['last_name']

    def __str__(self):
        return self.fieldName


class HealthCard(models.Model):
    userId = models.IntegerField(null=False)
    userFName = models.CharField(null=False, max_length=500)
    userLName = models.CharField(null=False, max_length=500)
    try:
        hcNo = models.IntegerField(default=randint(400000000000, 500000000000), unique=True, editable=False)
    except:
        pass

    def __str__(self):
        return str(self.hcNo)


class BookAppoinment(models.Model):
    bookId = models.AutoField(primary_key=True)
    patientId = models.IntegerField()
    patientName = models.CharField(max_length=300)
    doctorId = models.IntegerField()
    hcNo = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    payment = models.BooleanField()
    approve = models.BooleanField()
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    complateAppoinment = models.BooleanField()
    amount = models.IntegerField()

    def __str__(self):
        return "Booking ID : " + str(self.bookId) + " | " + str(self.hcNo)


class Prescriptions(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.IntegerField()
    appoId = models.IntegerField()
    tblName = jsonfield.JSONField()
    qty = jsonfield.JSONField()
    days = jsonfield.JSONField()
    tblTime = jsonfield.JSONField()

    def __str__(self):
        return "Prescription ID : " + str(self.appoId)

class MedicalReports(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.IntegerField()
    appoId = models.IntegerField()
    report = models.FileField()
    date = models.DateField(auto_now=False, auto_now_add=False , default="00-00-0000")
    desc = models.TextField()

    def __str__(self):
        return "Report ID : " + str(self.id) + " Patient ID : " + str(self.patientId)

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    appoId = models.IntegerField()
    patientId = models.IntegerField()
    patientName = models.CharField(max_length=500)
    doctorId = models.IntegerField()
    doctorName = models.CharField(max_length=500)
    date = models.DateField(auto_now=False, auto_now_add=False)
    hc = models.IntegerField()
    itemName = jsonfield.JSONField()
    itemBill = jsonfield.JSONField()
    totalBill = models.IntegerField()

    def __str__(self):
        return "ID : " +  str(self.patientId) + " | Name : " + str(self.patientName)
    