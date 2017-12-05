from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.shortcuts import redirect
from core.factory import AbstractFactory
from .forms import PostAdminForm, CategoryAdminForm, HeaderPageAdminForm, FooterPageAdminForm
from crispy_forms.utils import render_crispy_form
from jsonview.decorators import json_view
from django.template.context_processors import csrf
from django.db.models import Count
from django.http import Http404
from constance import config
from core.abstract_views import *
from core.mixins import StaffOnlyMixin
from django.contrib.admin.views.decorators import staff_member_required


###################################################################################
################################### BACKOFFICE ####################################
###################################################################################

############## ITEMS ##############
class PostListView(StaffOnlyMixin, AbstractModelListView):
    model_class = Post
    template = 'page/admin/post/list.html'


class PostCreateView(StaffOnlyMixin, AbstractModelCreateView):
    template = 'page/admin/post/form.html'
    model_form_class = PostAdminForm
    category_form_class = CategoryAdminForm
    redirection_url = 'page:post_list_admin'


@staff_member_required
def post_update_admin(request, post_id):
    return abstract_model_update(request, Post, post_id, PostAdminForm, 'page/admin/post/form.html',
                                 'page:post_list_admin', CategoryAdminForm)


@staff_member_required
def post_clone_admin(request, post_id):
    return abstract_model_clone(request, Post, post_id, PostAdminForm, 'page/admin/post/form.html',
                                 'page:post_list_admin', CategoryAdminForm)


@staff_member_required
def post_revert_admin(request, post_id, history_id):
    return abstract_model_revert(request, Post, post_id, history_id, PostAdminForm, 'page/admin/post/form.html',
                                'page:post_list_admin', CategoryAdminForm)


@staff_member_required
def post_restore_admin(request, history_id):
    return abstract_model_restore(request, Post, history_id, PostAdminForm, 'page/admin/post/form.html',
                                 'page:post_list_admin', CategoryAdminForm)


@staff_member_required
def post_delete_admin(request, post_id):
    return abstract_model_delete(request, Post, post_id, 'page:post_list_admin')


@staff_member_required
@json_view
def post_swap_position_admin(request, post_id, position):
    post = get_object_or_404(Post, id=post_id)
    post.to(int(position))
    return {'success': True, 'item_title': post.title, 'position': position}


############## CONFIGURATION ##############
@staff_member_required
def config_header_admin(request):
    if request.method == 'POST':
        form = HeaderPageAdminForm(request.POST)
        if form.is_valid():
            config.PAGE_HEADER = form.cleaned_data['body']
            messages.success(request, _("You have modified your header on each page"))
            return redirect('page:post_list_admin')
    else:
        form = HeaderPageAdminForm(initial={'body': config.PAGE_HEADER})
    return render(request, 'page/admin/config/header_form.html', {'form': form })


@staff_member_required
def config_footer_admin(request):
    if request.method == 'POST':
        form = FooterPageAdminForm(request.POST)
        if form.is_valid():
            config.PAGE_FOOTER = form.cleaned_data['body']
            messages.success(request, _("You have modified your footer on each page"))
            return redirect('page:post_list_admin')
    else:
        form = FooterPageAdminForm(initial={'body': config.PAGE_FOOTER})
    return render(request, 'page/admin/config/footer_form.html', {'form': form })


############## CATEGORIES ##############
@staff_member_required
def category_list_admin(request):
    categories = Category.objects.all()
    deleted_categories = Category.history.filter(history_type='-').order_by('-history_id')
    return render(request, 'page/admin/category/list.html', {'categories': categories, 'nodes': categories, 'deleted_categories': deleted_categories})


class CategoryPostCreateView(StaffOnlyMixin, AbstractModelCreateView):
    template = 'page/admin/category/form.html'
    model_form_class = CategoryAdminForm
    redirection_url = 'page:category_list_admin'


@staff_member_required
def category_update_admin(request, category_id):
    return abstract_model_update(request, Category, category_id, CategoryAdminForm, 'page/admin/category/form.html',
                                 'page:category_list_admin')


@staff_member_required
def category_delete_admin(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.warning(request, _("You have deleted category : " + category.title))
    return redirect('page:category_list_admin')


@staff_member_required
def category_revert_admin(request, post_id, history_id):
    category = get_object_or_404(Category, id=post_id)
    historical_category = Category.history.get(history_id=history_id)
    category_form = AbstractFactory.upsert(request, CategoryAdminForm, category, historical_category)
    if category_form.is_valid():
        messages.success(request, _("You have revert category : " + category.title))
        return redirect('page:category_list_admin')

    return render(request, 'page/admin/item/form.html', {'form': category_form, 'action': _("Revert")})


@staff_member_required
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


@staff_member_required
@json_view
def ajax_category_move(request, node_from_id, node_to_id, action):
    if action == 'after':
        action = 'right'
    elif action == 'before':
        action = 'left'
    else:
        action = 'first-child'

    node_from = get_object_or_404(Category, id=node_from_id)
    node_to = get_object_or_404(Category, id=node_to_id)
    node_from.move_to(node_to, action)
    return {'success': True}

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