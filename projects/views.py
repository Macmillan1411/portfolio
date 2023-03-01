from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Project

# Create your views here.
class ProjectsView(ListView):
    model = Project
    template_name = 'projects_index.html'

class ProjectsDetailView(DetailView):
    model = Project
    template_name = 'projects_detail.html'