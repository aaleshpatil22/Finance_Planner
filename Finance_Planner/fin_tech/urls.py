from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='sample'),
    path('show_details', views.show_details, name='show_details'),
]
