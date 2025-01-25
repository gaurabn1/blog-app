from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone
from .models import Blog

def post_list(request):
    posts = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page', 1)
    print(page_number)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})
