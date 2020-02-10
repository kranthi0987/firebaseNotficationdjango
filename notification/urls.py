from django.urls import path

from notification.views import Notifcationapi

urlpatterns = [
    path('notification/', Notifcationapi.as_view()),

]