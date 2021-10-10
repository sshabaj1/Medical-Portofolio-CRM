from django.urls import path
from website.views import LandindPageView

app_name = 'website'

urlpatterns = [

    path('', LandindPageView.as_view(), name='landind_page')

]
