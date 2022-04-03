from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.display_words,name='display_words'),
    path('word_form',views.word_form,name="word_form"),
    path('update_word/<str:pk>/',views.update_word,name='update_word'),
    path('delete_word/<str:pk>/',views.delete_word,name='delete_word')
]