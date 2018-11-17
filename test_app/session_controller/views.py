from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserSessionStore


class IndexView(LoginRequiredMixin,ListView):

    model = UserSessionStore
    template_name = 'index.html'
