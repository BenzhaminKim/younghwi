from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import (
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.

def home(request):
    return render(request,'webapp/home.html')

@login_required
def note(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'webapp/note.html',context)

def about(request):
    return render(request, 'webapp/about.html')

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'webapp/note.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/note'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
