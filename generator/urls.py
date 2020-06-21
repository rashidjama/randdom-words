from django.urls import path
from . import views


urlpatterns = [
  path('', views.words),
  path('words', views.words),
  path('click', views.click),
  path('reset', views.reset)
]