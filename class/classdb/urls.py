from django.urls import path
from . import views


app_name = "classdb"
urlpatterns = [
    path("", views.index, name="index"),
    path('<int:id>/', views.index1, name='index1'),
    ]