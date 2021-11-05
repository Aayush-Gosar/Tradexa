from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from users.models import CustomUser
# Create your views here.
'''
posts = [
    {
        'user' : 'Ankit',
        'title' : 'Blog Post 1',
        'content' : 'First post content',Lo
        'date_posted' : '1 Dec 2000'
    },
    {
        'user' : 'Vishal',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : '8 May 1995'
    }

'''

def home(request):
    #a = 5
    #b= 7
    #return HttpResponse('<h1> Sum: '+ str(a+b) + '</h1>')
    #return HttpResponse('<h1>Blog Home</h1>')
    context = {
    'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app><model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app><model>_<viewtype>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted']
    paginate_by = 3
    
    def get_queryset(self):
        user = get_object_or_404(CustomUser, username = self.kwargs.get('username'))
        return Post.objects.filter(user=user).order_by('-created_at')    


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['text']
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['text']
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request,'blog/about.html',{'title' : 'About'})