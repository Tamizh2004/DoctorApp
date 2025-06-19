from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login_page,name='login'),
    path('signup/',views.signup_page,name='signup'),
    path('home/',views.home_page,name='home'),
    path('register/',views.register_page,name='register'),
    path('form/<int:id>',views.form,name='form'),
    path('slot/',views.slot_page,name='slot'),
    path('Alogin/',views.Alogin_page,name='Alogin')
]