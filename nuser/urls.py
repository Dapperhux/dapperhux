from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('vip/', views.vip, name='vip'),
    path('staff/', views.staff, name='staff'),
    path('vip_staff/', views.vip_staff, name='vip_staff'),
    path('test_staff/', views.test_staff, name='test_staff'),
    path('daily_staff/', views.daily_staff, name='daily_staff'),
    path('pvip/', views.pvip, name='pvip'),
    path('plan_a/', views.plan_a, name='plan_a'),
    path('plan_b/', views.plan_b, name='plan_b'),
    path('plan_c/', views.plan_c, name='plan_c'),
    path('contact/', views.contact, name='contact'),
    path('about_us/', views.about_us, name='about_us'),
]