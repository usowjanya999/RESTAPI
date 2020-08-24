from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from .serializers import PatientSerializer,DoctorSerializer,AppointmentSerializer
from .models import Patient,Doctor,Appointment


class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DoctorView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class AppointmentView(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class viewdata(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
       
        queryset = Appointment.objects.all()
        Doctor= self.request.query_params.get('doctor', None)
        if Doctor is not None:
            queryset = queryset.filter(doctor=Doctor)
        return queryset


