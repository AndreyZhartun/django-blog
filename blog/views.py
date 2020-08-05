from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from itertools import repeat

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date').reverse()
    if len(posts) > 10:
        posts = posts[:10]
    return render(request, 'home.html', {'object_list': posts})

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})