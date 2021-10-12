from django.urls import path
from .views import DashboardView, UserCreateView, UserLoginView, logout_request, UserCreateView


app_name = 'users'

urlpatterns = [

    path('', DashboardView.as_view(), name='dashboard'),
    path('loggin/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_request, name='logout'),
    path('create-user/', UserCreateView.as_view(), name='create-user')


]
