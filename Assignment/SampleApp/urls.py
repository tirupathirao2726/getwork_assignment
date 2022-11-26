from django.urls import path
from . import views
app_name="SampleApp"
urlpatterns=[
    path("",views.home,name="index"),
    path("get_data/",views.get_data,name="get_data"),
]
