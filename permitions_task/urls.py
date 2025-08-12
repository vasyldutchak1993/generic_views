from django.urls import path

from permitions_task.views import ArticleListView, ArticleDetailView, edit_article, delete_article

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit/', edit_article, name='article_edit'),
    path('<int:pk>/delete/', delete_article, name='article_delete'),
]
