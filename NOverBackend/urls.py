from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("ssadmiin", admin.site.urls),
    path("",index),
    path('Ask-Ai-Api/',ask_ai, name='ask_ai'),
]
