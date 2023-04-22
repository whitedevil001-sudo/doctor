from django.contrib import admin
from django.urls import path, include
from api.views import doctor_viewset#parchi_viewset
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'doctors',doctor_viewset)
#router.register(r'appontment',parchi_viewset)
urlpatterns = [
    path('',include(router.urls))
]
