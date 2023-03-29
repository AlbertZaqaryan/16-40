from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('brand/<int:id>/', views.index_detail, name='index_detail'),
]