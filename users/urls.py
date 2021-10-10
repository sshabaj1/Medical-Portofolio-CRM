from django.urls import path
from .views import DashboardView, UserLoginView, logout_request


app_name = 'users'

urlpatterns = [

    path('', DashboardView.as_view(), name='dashboard'),
    path('loggin/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_request, name='logout')


]
