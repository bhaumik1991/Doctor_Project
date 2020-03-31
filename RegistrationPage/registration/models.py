from django.db import models
from django.urls import reverse,reverse_lazy

# Create your models here.
class Doctor(models.Model):
    full_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50)
    dob = models.DateField(max_length=8)
    phone_number = models.TextField(max_length=10)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)
    hospital_name = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class Prescription(models.Model):
    patient_name = models.CharField(max_length=20, unique=True)
    phone_number1 = models.TextField(max_length=10)
    age = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    mediciene_name = models.CharField(max_length=100)
    mediciene_power = models.CharField(max_length=10)
    dose = models.CharField(max_length=10)
    day = models.CharField(max_length=10)
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.patient_name