from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('career/', views.career, name='career'),
    path('love/', views.love, name='love'),
    path('health/', views.health, name='health'),
    path('finance/', views.finance, name='finance'),
    path('reading/<slug1>/<slug2>', views.reading, name='reading'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)




