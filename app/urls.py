from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.ResumeContactView.as_view(), name="home"),
]