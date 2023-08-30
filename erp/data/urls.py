from django.urls import path
from data.views import index

urlpatterns = [
    path('index/', index),

]
