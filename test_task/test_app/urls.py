from django.urls import path
from . import views

urlpatterns = [
    path('get_all_books/', views.get_all_books),
    path('get_book/<int:book_id>/', views.get_book),

               ]
