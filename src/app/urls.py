from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('_<slug:slug>/', views.gateway, name="gateway"),
    path('<slug:slug>/', views.redirection, name="redirection"),
]
