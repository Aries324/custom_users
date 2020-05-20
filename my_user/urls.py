from django.urls import path
from my_user import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logged_out/', views.logged_outview, name='logged_out'),



]
