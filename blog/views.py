from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogType
from django.core.paginator import Paginator


def blog_list(requests):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 1)
    page_num = requests.GET.get('page', 1)
    print(page_num)
    blog_pages = paginator.get_page(page_num)
    blog_types = BlogType.objects.all()
    print(blogs)
    print(blog_pages.object_list)
    return render(requests, "blog/blog_list.html", {
        "blog_types": blog_types,
        "blog_pages": blog_pages
    })


def blog_detail(requests, blog_id):
    return render(requests, "blog/blog_detail.html",
                  {'blog': get_object_or_404(Blog, id=blog_id)})


def blog_type_list(requests, blog_type_id):
    blog_type = get_object_or_404(BlogType, id=blog_type_id)
    blogs = Blog.objects.filter(blog_type=blog_type.id)
    blog_types = BlogType.objects.all()
    return render(requests, 'blog/blog_type_list.html', {
        'blog_type': blog_type,
        'blogs': blogs,
        "blog_types": blog_types
    })
