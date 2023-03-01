from django.urls import path
from .views import ProjectsView,ProjectsDetailView

urlpatterns = [
    path('',ProjectsView.as_view(),name = 'projects_index'),
    path('<int:pk>',ProjectsDetailView.as_view(),name = 'projects_detail'),
]
