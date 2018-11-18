from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserSessionStore
from .session_decorators import unique_session
from django.views import View
from django.contrib.auth.decorators import login_required

class IndexView(LoginRequiredMixin, ListView):

    model = UserSessionStore
    template_name = 'index.html'

    @unique_session
    def get(self, request, *args, **kwargs):
        print("index view called")
        # import pdb;pdb.set_trace()
        sessions = UserSessionStore.objects.filter(user=request.user).order_by("-created_at")
        return render(request, self.template_name, {"object_list": sessions})


class UnControlledView(LoginRequiredMixin, ListView):

    model = UserSessionStore
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        print("uncontrolled view called")
        # import pdb;pdb.set_trace()
        sessions = UserSessionStore.objects.filter(user=request.user).order_by("-created_at")
        return render(request, self.template_name, {"object_list": sessions})

def sample_view(request):
    print("sample view")
    return HttpResponse("sample view")


# @login_required
# @unique_session
# def test_view(request):
#     return HttpResponse("success")