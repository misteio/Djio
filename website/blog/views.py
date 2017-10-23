from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.shortcuts import redirect
from .factory import BlogFactory


@permission_required(('admin'), '/admin/login')
def post_list_admin(request):
    posts = Post.admin_load.all()
    return render(request, 'blog/admin/post/list.html', {'posts': posts})


@permission_required(('admin'), '/admin/login')
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, 'blog/admin/post/detail.html', {'post': post})


@permission_required(('admin'), '/admin/login')
def post_form_admin(request):
    post_form = BlogFactory.upsert(request)
    if post_form.is_valid():
        messages.success(request, _("You have create a new post"))
        return redirect('blog:post_list_admin')
    return render(request, 'blog/admin/post/form.html', {'form': post_form})


@permission_required(('admin'), '/admin/login')
def post_update_admin(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_form = BlogFactory.upsert(request, post)
    if post_form.is_valid():
        messages.success(request, _("You have update post : " + post.title))
        return redirect('blog:post_list_admin')

    return render(request, 'blog/admin/post/form.html', {'form': post_form})


@permission_required(('admin'), '/admin/login')
def post_clone_admin(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_form = BlogFactory.upsert(request, post)
    if post_form.is_valid():
        messages.success(request, _("You have clone post : " + post.title))
        return redirect('blog:post_list_admin')

    return render(request, 'blog/admin/post/form.html', {'form': post_form})


@permission_required(('admin'), '/admin/login')
def post_delete_admin(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.warning(request, _("You have deleted post : " + post.title))
    return redirect('blog:post_list_admin')

