from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from api.models import doctors#appointment

from api.serializer import doctorserializer#appointmentserializers
class doctor_viewset(viewsets.ModelViewSet):
    queryset=doctors.objects.all()
    serializer_class=doctorserializer

'''class parchi_viewset(viewsets.ModelViewSet):
    queryset=appointment.objects.all()
    serializer_class=appointmentserializers'''