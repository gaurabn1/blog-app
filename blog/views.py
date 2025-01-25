from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogForm

def post_list(request):
    posts = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def post_detail(request, id):
    post = get_object_or_404(Blog, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = BlogForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method =='POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)

    else:
        form = BlogForm(instance=post)
    return render(request, 'blog/post_new.html', {'form':form})
