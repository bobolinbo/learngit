'''为应用程序users定义URL模式'''
from django.contrib.auth.views import LoginView

from django.urls import path,include

from . import views
LoginView.template_name = 'users/login.html'
app_name = 'users'
urlpatterns = [
    #登入页面
    path('login/',LoginView.as_view(),name = 'login'),
    path('logout/',views.logout_view,name = 'logout'),
    path('register/',views.register,name = 'register'),

]