from django.urls import path
from .views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view(), name='article-list'),
    path('<slug:slug>/', ArticleView.as_view(), name='article-detail'),
]

# urlpatterns = [
#     path('', ArticleView.as_view(), name='article-list'),
#     path('<slug:slug>/', ArticleView.as_view(), name='article-detail'),
# ]