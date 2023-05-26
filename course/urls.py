# from django.urls import path
# from .views import CourseListView, CourseDetailView

# urlpatterns = [
#     path('', CourseListView.as_view(), name='course-list'),
#     path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
# ]

from django.urls import path
from .views import CourseListView, ChapterListView, CourseDetailView

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('<int:id>/chapters/', ChapterListView.as_view(), name='chapter-list'),
]
