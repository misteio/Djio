from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import PostAdminForm

class BlogFactory():
    def upsert(request, post=None):
        if request.method == 'POST':
            author = get_object_or_404(User, id=request.POST.get("author"))
            if post:
                if 'clone' in request.path:
                    post_form = PostAdminForm(data=request.POST)
                else:
                    post_form = PostAdminForm(data=request.POST, instance=post)
            else:
                post_form = PostAdminForm(data=request.POST)

            if post_form.is_valid():
                _post = post_form.save(commit=False)
                _post.author = author
                _post.save()
            else:
                return post_form
        else:
            if post:
                post_form = PostAdminForm(instance=post)
            else:
                post_form = PostAdminForm()

        return post_form