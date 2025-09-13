from django.urls import include, path

from pages import views

urlpatterns = [
  path("", views.home, name="home"),
  ]