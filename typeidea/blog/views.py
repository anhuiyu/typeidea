from django.shortcuts import render
from .models import Post,Tag,Category
from django.http import HttpResponse
# Create your views here.

def post_list(request, category_id=None,tag_id=None):
    tag=None
    category=None
    if tag_id:
        post_list,tag=Post.get_by_tag(tag_id)
    elif category_id:
        post_list,category=Post.get_by_category(category_id)
    else:
        post_list=Post.latest_posts()
    context= {
        'post_list': post_list,
        'category': category,
        'tag': tag
    }
    context.update(Category.get_navs())
    return render(request,'blog/list.html',context=context)
def post_detail(request, post_id=None):
    try:
        post=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post=None
    context={
        'post':post,
    }
    context.update(Category.get_navs())
    return render(request,'blog/detail.html',context=context)


