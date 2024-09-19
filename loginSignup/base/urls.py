from django.urls import path,include
from .views import authview, home
urlpatterns =[
    path("",home,name="home"),
    path("signup/",authview,name="authview"),
    path("accounts/",include("django.contrib.auth.urls")),


]