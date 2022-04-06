
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hello',views.hello_world),
    path('',views.home_page),
    path('task',views.task),
    path('all-analytics',views.all_analytics),
    path('<slug:shorturl>', views.redirect_url)
]
