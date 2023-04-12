from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('hello/', views.hello),
    path('number/', views.evenodd),
    path('index/',views.index),
    path('table/', views.table),
    path('var/', views.variables),
    path('emp/', views.employees),
    path('images/', views.images),
    path('', views.background),
    path('members/', views.members),

]