
from django.contrib import admin
from django.urls import path, include
from BucketApp import views 


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',views.start, name='start'),
    path('bucket/', include('BucketApp.BucketUrls'))
]
