
from django.urls import path
from bnpl import views

urlpatterns = [
    path('', views.home),
    path('buy', views.buy)
]