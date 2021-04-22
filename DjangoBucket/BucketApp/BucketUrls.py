from django.urls import path
from . import views

app_name='BucketApp'

urlpatterns=[
    path('start/',views.start,name='BucketStart'),
    path('create/category',views.createCategory,name='createCategory'),
    path('delete/category/<int:pk>/', views.DeleteCategoryView.as_view()),
    path('create/item/',views.createItem,name='createItem'),
    path('link/<int:pk1>/<int:pk2>',views.link,name='Link'),
    path('delete/item/<int:pk>/', views.DeleteItemView.as_view()),
    path('uncouple/item/<int:pk>/<int:pk2>/', views.DeleteItemView.as_view()),
]