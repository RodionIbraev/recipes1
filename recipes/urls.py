from django.contrib import admin
from django.urls import path, re_path
from calculator.views import handler_view

urlpatterns = [
    path('<str:recipe>/', handler_view, name='recipe'),
    path('admin/', admin.site.urls),
]