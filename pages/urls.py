from django.urls import include, path


from pages import views

urlpatterns = [
  path("", views.home, name="home"),
  path("about", views.about, name="about"),
  path("services", views.services, name="services"),
  path("contact", views.contact, name="contact"),
  path("cars", views.cars, name="cars"),
  ]