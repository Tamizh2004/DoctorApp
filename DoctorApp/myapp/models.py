from django.db import models

# Create your models here.
class Userdata(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.email

class Userdata2(models.Model):
    doctor_name=models.CharField(max_length=100)
    doctor_img=models.ImageField(upload_to='doctors/')
    spec=models.CharField(max_length=50)
    def __str__(self):
        return self.doctor_name
    
class PatientDetails(models.Model):
    doc_name=models.CharField(max_length=100)
    patient_name=models.CharField(max_length=100)
    age=models.CharField(max_length=50)
    gender=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    problem=models.CharField(max_length=100)
    def __str__(self):
        return self.patient_name

class Alogin(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.email