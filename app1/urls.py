from django.urls import path
from app1.views import *
app_name='something1'
urlpatterns=[
    path('st1files/',st1files,name='st1files'),
]