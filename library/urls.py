from django.urls import path
from .views import book_list, upload_book, delete_book, delete_all_books

urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('upload_book/', upload_book, name='upload_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
    path('delete_all_books/', delete_all_books, name='delete_all_books'),
    # 添加一個空路徑的處理
    path('', book_list, name='home'),  # 將空路徑導向到 book_list 函數
]
