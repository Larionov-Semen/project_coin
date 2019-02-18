from django.urls import path
from . import views

app_name = 'auction'

urlpatterns = [
    path('', views.Index.as_view()),
]
