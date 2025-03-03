from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('career/', views.career, name='career'),
    path('love/', views.love, name='love'),
    path('health/', views.health, name='health'),
    path('finance/', views.finance, name='finance'),
    path('reading/<slug1>/<slug2>', views.reading, name='reading'),
] 




