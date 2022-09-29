from django.urls import path
from . import views

urlpatterns=[
    path('articulo/', views.list, name='list_articles'),
    path('categoria/<int:category_id>', views.category, name='category'),
    path('articulo/<int:article_id>', views.article, name='articulo'),
]
