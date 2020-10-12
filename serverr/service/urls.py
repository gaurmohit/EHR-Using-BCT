from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start, name='start'),
    path('status/<int:id>/', views.status, name='status'),
    path('', views.service, name='service'),
    path('show_all/', views.show_all, name='show_all'),
    path('delete/', views.del_all, name='delete'),
]
