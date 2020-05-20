from django.urls import path
from my_user import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('signup/', views.signup_view),
    path('login/', views.loginview),
    path('logged_out/', views.logged_outview),



]
