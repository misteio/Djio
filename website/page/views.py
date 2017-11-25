from django.shortcuts import render, get_object_or_404
from .models import Post, Category, User
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.shortcuts import redirect
from core.factory import AbstractFactory
from core.utils import create_action
from .forms import PostAdminForm, CategoryAdminForm
from crispy_forms.utils import render_crispy_form
from jsonview.decorators import json_view
from django.template.context_processors import csrf
from django.db.models import Count
from django.core.mail import send_mail
from django.conf import settings
from django.http import Http404

###################################################################################
################################### BACKOFFICE ####################################
###################################################################################

############## ITEMS ##############
@permission_required(('admin'), '/admin/login')
def post_list_admin(request):
    posts = Post.objects.select_related('author').all()
    deleted_posts = Post.history.filter(history_type='-').order_by('-history_id')
    return render(request, 'page/admin/post/list.html', {'posts': posts, 'deleted_posts': deleted_posts })


@permission_required(('admin'), '/admin/login')
def post_create_admin(request):
    category_form = AbstractFactory.upsert(request, CategoryAdminForm)
    post_form = AbstractFactory.upsert(request, PostAdminForm)
    if post_form.is_valid():
        messages.success(request, _("You have create a new post"))
        return redirect('page:post_list_admin')
    return render(request, 'page/admin/post/form.html', {'form': post_form, 'category_form': category_form, 'action': _("Create")})


@permission_required(('admin'), '/admin/login')
def post_update_admin(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_form = AbstractFactory.upsert(request, PostAdminForm, post)
    category_form = AbstractFactory.upsert(request, CategoryAdminForm)
    if post_form.is_valid():
        messages.success(request, _("You have update post : " + post.title))
        return redirect('page:post_list_admin')

    historical_items = Post.history.filter(id=post_id).order_by('-history_id')
    return render(request, 'page/admin/post/form.html', {'form': post_form, 'category_form': category_form, 'historical_items': historical_items, 'action': _("Update")})


@permission_required(('admin'), '/admin/login')
def post_clone_admin(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_form = AbstractFactory.upsert(request, PostAdminForm, post)
    category_form = AbstractFactory.upsert(request, CategoryAdminForm)
    if post_form.is_valid():
        messages.success(request, _("You have clone post : " + post.title))
        return redirect('page:post_list_admin')

    return render(request, 'page/admin/post/form.html', {'form': post_form, 'category_form': category_form, 'action': _("Clone")})


@permission_required(('admin'), '/admin/login')
def post_revert_admin(request, post_id, history_id):
    post = get_object_or_404(Post, id=post_id)
    historical_item = Post.history.get(history_id=history_id)
    post_form = AbstractFactory.upsert(request, PostAdminForm, post, historical_item)
    category_form = AbstractFactory.upsert(request, CategoryAdminForm)
    if post_form.is_valid():
        messages.success(request, _("You have clone post : " + post.title))
        return redirect('page:post_list_admin')

    return render(request, 'page/admin/post/form.html', {'form': post_form, 'category_form': category_form, 'action': _("Revert")})


@permission_required(('admin'), '/admin/login')
def post_delete_admin(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.warning(request, _("You have deleted item : " + post.title))
    return redirect('page:post_list_admin')


@permission_required(('admin'), '/admin/login')
@json_view
def post_swap_position_admin(request, post_id, position):
    post = get_object_or_404(Post, id=post_id)
    post.to(int(position))
    return {'success': True, 'item_title': post.title, 'position': position}


############## CATEGORIES ##############
@permission_required(('admin'), '/admin/login')
def category_list_admin(request):
    categories = Category.objects.all()
    deleted_categories = Category.history.filter(history_type='-').order_by('-history_id')
    return render(request, 'page/admin/category/list.html', {'categories': categories, 'deleted_categories': deleted_categories})


@permission_required(('admin'), '/admin/login')
def category_create_admin(request):
    category_form = AbstractFactory.upsert(request, CategoryAdminForm)
    if category_form.is_valid():
        messages.success(request, _("You have create a new category"))
        return redirect('page:category_list_admin')
    return render(request, 'page/admin/category/form.html', {'form': category_form, 'action': _("Create")})


@permission_required(('admin'), '/admin/login')
def category_update_admin(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category_form = AbstractFactory.upsert(request, CategoryAdminForm, category)
    if category_form.is_valid():
        messages.success(request, _("You have update category : " + category.title))
        return redirect('page:category_list_admin')

    historical_items = Category.history.filter(id=category_id).order_by('-history_id')
    return render(request, 'page/admin/category/form.html', {'form': category_form, 'historical_items': historical_items, 'action': _("Update")})


@permission_required(('admin'), '/admin/login')
def category_delete_admin(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.warning(request, _("You have deleted category : " + category.title))
    return redirect('wishlist:category_list_admin')


@permission_required(('admin'), '/admin/login')
def category_revert_admin(request, post_id, history_id):
    category = get_object_or_404(Category, id=post_id)
    historical_category = Category.history.get(history_id=history_id)
    category_form = AbstractFactory.upsert(request, CategoryAdminForm, category, historical_category)
    if category_form.is_valid():
        messages.success(request, _("You have revert category : " + category.title))
        return redirect('wishlist:category_list_admin')

    return render(request, 'wishlist/admin/item/form.html', {'form': category_form, 'action': _("Revert")})


@permission_required(('admin'), '/admin/login')
@json_view
def ajax_category_save(request):
    form = CategoryAdminForm(request.POST or None)
    if form.is_valid():
        category = form.save()
        return {'success': True, 'category_id': category.id, 'category_title': category.title}

    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)
    return {'success': False, 'form_html': form_html}


###################################################################################
################################### FRONT #########################################
###################################################################################
def page_post_list_category(request, category_slug):
    categories = Category.objects.annotate(num_items=Count('category_items')).filter(status='published')
    items = Post.objects.prefetch_related('participate').select_related('category').filter(status='published', category__slug=category_slug)
    if len(items) == 0:
        raise Http404("Category not found")
    return render(request, 'wishlist/front/items/list.html', {'categories': categories, 'items': items })


def post_detail(request, post_slug):
    post = get_object_or_404(Post.objects.filter(slug=post_slug))
    return render(request, 'page/front/post/detail.html', {'post': post })


def home_page(request):
    post = Post.objects.filter(slug='home').first()
    return render(request, 'page/front/post/detail.html', {'post': post })