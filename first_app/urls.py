from django.conf.urls import url
from first_app import views

app_name = "first_app"

urlpatterns = [
    url(r'^$', views.main, name = 'main'),
    url(r'^userlogin/$', views.UserLoginView, name='userlogin'),
    url(r'^userlogout/$', views.UserLogoutView, name='userlogout'),
    url(r'^register/$', views.RegisterView, name='register'),
    url(r'^registers/$', views.RegisteredUsersView, name='registers')
]
