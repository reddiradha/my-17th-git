from django.urls import path
from app2.views import *
app_name='something2'
urlpatterns=[
    path('st2files/',st2files,name='st2files'),
]