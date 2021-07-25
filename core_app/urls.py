from django.urls import path
from core_app.apps import CoreAppConfig
from core_app import views

app_name = CoreAppConfig.name

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]
