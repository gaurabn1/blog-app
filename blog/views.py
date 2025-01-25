from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Blog

def post_list(request):
    posts = Blog.objects.filter(published_date__isnull=False)
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})
