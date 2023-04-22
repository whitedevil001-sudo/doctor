from rest_framework import serializers
from api.models import doctors#appointment
class doctorserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=doctors
        fields="__all__"

'''class appointmentserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=appointment
        fields="__all__"'''
