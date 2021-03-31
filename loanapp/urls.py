from django.urls import path
from . import views


urlpatterns=[
    path('chart.html', views.chart, name='Charts'),
    path('', views.home, name='Home'),
    path('index.html', views.index,name='Predict'),
    path('Result.html', views.result, name='Result'),
    path('Contact.html', views.contact,name='Contact'),
    path('About.html', views.about,name='About'),
]
