from django.urls import path
from . import views, views_admin, views_logon
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Login logic
    path('', views_logon.index, name='index'),
    path('register/', views_logon.register, name='register'),

    path('administrator/', views_admin.start, name='admin_panel'),
    path('administrator/<slug:slug>/', views_admin.staff, name='staff'),
    path('administrator/<slug:slug>/', views_admin.order, name='order'),

    path('select/', views.start, name='user_panel'),


    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
          
]
