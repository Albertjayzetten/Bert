from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('clothing/', views.clothing, name="clothing"),
    path('login/', views.login, name="login"),
    path('sign-up/', views.signup, name="signup"),

    path('clothing/list/', views.admin_clothing, name='clothing_list'),
    path('clothing/add/', views.admin_clothing_add, name='clothing_add'),
    path('clothing/edit/<int:clothing_id>/', views.admin_clothing_edit, name='clothing_edit'),
    path('clothing/delete/<int:clothing_id>/', views.admin_clothing_delete, name='clothing_delete'),

    path('clothing/<int:clothing_id>/image/<int:image_id>/', views.admin_clothing_image_delete, name='image_delete'),
]