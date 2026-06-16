from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('summary/create/', views.create_summary, name='create_summary'),
    path('mindmap/create/', views.create_mindmap, name='create_mindmap'),
    path('studyplan/create/', views.create_studyplan, name='create_studyplan'),
    path('reminder/create/', views.create_reminder, name='create_reminder'),
]