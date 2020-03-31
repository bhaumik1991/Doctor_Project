from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/',views.login, name='login'),
    # path('logout/', views.Logout, name='logout'),
    path('prescription/', views.prescription, name='prescription'),
    path('prescription_create/', views.prescription_create, name='prescription_create'),
    # path('show_prescription/', views.show_prescription, name='show_prescription'),

]