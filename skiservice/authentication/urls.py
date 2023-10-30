from django.urls import path
from . import views, views_admin, views_logon


urlpatterns = [
    # Login logic
    path('', views_logon.index, name='index'),
    path('register/', views_logon.register, name='register'),
          
]
