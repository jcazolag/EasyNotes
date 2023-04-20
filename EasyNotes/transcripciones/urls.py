from django.urls import path
from . import views

urlpatterns = [
    path('', views.whisper, name='whisper'),
    path('notes', views.Notes, name='notes'),
    path('<int:transcripcion_id>', views.detail, name='detail'),
]