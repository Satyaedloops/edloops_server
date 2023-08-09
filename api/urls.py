from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('account/', include('account.urls')),
    path('course/', include('course.urls')),
    path('blogs/', include('blog.urls')),
] 