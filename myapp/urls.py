
from django.contrib import admin
from django.urls import path
from .views import home, upload_image
from . import views


urlpatterns = [
    # path('',home,name='home'),
    # path('update/<int:id>/',home,name='update_student')
    path('upload/', views.upload_image, name="upload_image"),

]

