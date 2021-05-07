from django.urls import path
from . import views

app_name='D3App'

urlpatterns=[

    path('bubbles', views.bubbles, name='bubbles'),
    path('createBubble', views.createBubble, name='createBubble'),
    path('delete/bubble/<int:pk>/', views.DeleteBubbleView.as_view()),
    path('singleBubble/<int:pk>', views.singleBubble, name='singleBubble'),
    path('changeBubble', views.changeBubble, name='changeBubble'),





]

