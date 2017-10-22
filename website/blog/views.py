from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from .forms import PostAdminForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required


@permission_required(('admin'), '/admin/login')
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/admin/post/list.html', {'posts': posts})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'blog/admin/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, 'blog/admin/post/detail.html', {'post': post})


def post_form_admin(request):
    if request.method == 'POST':
        author = get_object_or_404(User, id=request.POST.get("author"))
        post_form = PostAdminForm(data=request.POST)

        if post_form.is_valid():
            # Create Comment object but don't save to database yet
            new_post = post_form.save(commit=False)
            new_post.author = author
            # Save the comment to the database
            new_post.save()
    else:
        post_form = PostAdminForm()

    return render(request, 'blog/admin/post/form.html', {'form': post_form})


def post_update_admin(request, post_id):
    if request.method == 'POST':
        author = get_object_or_404(User, id=request.POST.get("author"))
        post = get_object_or_404(Post, id=post_id)
        post_form = PostAdminForm(data=request.POST, instance=post)

        if post_form.is_valid():
            # Create Comment object but don't save to database yet
            update_post = post_form.save(commit=False)
            update_post.author = author
            update_post.save()
    else:
        _post = get_object_or_404(Post, id=post_id)
        post_form = PostAdminForm(instance=get_object_or_404(Post, id=post_id))
        #post_form = PostAdminForm(instance=Post.history.get(id=14))

    return render(request, 'blog/admin/post/form.html', {'form': post_form})