from django.db import models


class Patient(models.Model):

    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class Doctor(models.Model):

    name = models.CharField(max_length=30)
    department = models.CharField(max_length=10)


def __str__(self):
        return self.name


class Appointment(models.Model):

    time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)



	
	


