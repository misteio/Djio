from django.shortcuts import render, get_object_or_404
from .models import Item, Category
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.shortcuts import redirect
from core.factory import AbstractFactory
from core.utils import create_action
from .forms import ItemAdminForm, CategoryAdminForm, BookItemForm
from crispy_forms.utils import render_crispy_form
from jsonview.decorators import json_view
from django.template.context_processors import csrf
from django.db.models import Count
from django.core.mail import send_mail
from django.conf import settings


###################################################################################
################################### BACKOFFICE ####################################
###################################################################################

############## ITEMS ##############
@permission_required(('admin'), '/admin/login')
def item_list_admin(request):
    items = Item.admin_load.all()
    deleted_items = Item.history.filter(history_type='-').order_by('-history_id')
    return render(request, 'wishlist/admin/item/list.html', {'items': items, 'deleted_items': deleted_items})


@permission_required(('admin'), '/admin/login')
def item_create_admin(request):
    category_form = AbstractFactory.upsert(request, CategoryAdminForm)
    item_form = AbstractFactory.upsert(request, ItemAdminForm)
    if item_form.is_valid():
        messages.success(request, _("You have create a new item"))
        return redirect('wishlist:item_list_admin')
    return render(request, 'wishlist/admin/item/form.html', {'form': item_form, 'category_form': category_form, 'action': _("Create")})


@permission_required(('admin'), '/admin/login')
def item_update_admin(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item_form = AbstractFactory.upsert(request, ItemAdminForm, item)
    category_form = AbstractFactory.upsert(request, CategoryAdminForm)
    if item_form.is_valid():
        messages.success(request, _("You have update item : " + item.title))
        return redirect('wishlist:item_list_admin')

    historical_items = Item.history.filter(id=item_id).order_by('-history_id')
    return render(request, 'wishlist/admin/item/form.html', {'form': item_form, 'category_form': category_form, 'historical_items': historical_items, 'action': _("Update")})


@permission_required(('admin'), '/admin/login')
def item_clone_admin(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item_form = AbstractFactory.upsert(request, ItemAdminForm, item)
    category_form = AbstractFactory.upsert(request, CategoryAdminForm)
    if item_form.is_valid():
        messages.success(request, _("You have clone item : " + item.title))
        return redirect('wishlist:item_list_admin')

    return render(request, 'wishlist/admin/item/form.html', {'form': item_form, 'category_form': category_form, 'action': _("Clone")})


@permission_required(('admin'), '/admin/login')
def item_revert_admin(request, item_id, history_id):
    item = get_object_or_404(Item, id=item_id)
    historical_item = Item.history.get(history_id=history_id)
    item_form = AbstractFactory.upsert(request, ItemAdminForm, item, historical_item)
    category_form = AbstractFactory.upsert(request, CategoryAdminForm)
    if item_form.is_valid():
        messages.success(request, _("You have clone item : " + item.title))
        return redirect('wishlist:item_list_admin')

    return render(request, 'wishlist/admin/item/form.html', {'form': item_form, 'category_form': category_form, 'action': _("Revert")})


@permission_required(('admin'), '/admin/login')
def item_delete_admin(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    messages.warning(request, _("You have deleted item : " + item.title))
    return redirect('wishlist:item_list_admin')


@permission_required(('admin'), '/admin/login')
@json_view
def item_swap_position_admin(request, item_id, position):
    item = get_object_or_404(Item, id=item_id)
    item.to(int(position))
    return {'success': True, 'item_title': item.title, 'position': position}


############## CATEGORIES ##############
@permission_required(('admin'), '/admin/login')
def category_list_admin(request):
    categories = Category.objects.all()
    deleted_categories = Category.history.filter(history_type='-').order_by('-history_id')
    return render(request, 'wishlist/admin/category/list.html', {'categories': categories, 'deleted_categories': deleted_categories})


@permission_required(('admin'), '/admin/login')
def category_create_admin(request):
    category_form = AbstractFactory.upsert(request, CategoryAdminForm)
    if category_form.is_valid():
        messages.success(request, _("You have create a new category"))
        return redirect('wishlist:category_list_admin')
    return render(request, 'wishlist/admin/category/form.html', {'form': category_form, 'action': _("Create")})


@permission_required(('admin'), '/admin/login')
def category_update_admin(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category_form = AbstractFactory.upsert(request, CategoryAdminForm, category)
    if category_form.is_valid():
        messages.success(request, _("You have update category : " + category.title))
        return redirect('wishlist:category_list_admin')

    historical_items = Category.history.filter(id=category_id).order_by('-history_id')
    return render(request, 'wishlist/admin/category/form.html', {'form': category_form, 'historical_items': historical_items, 'action': _("Update")})


@permission_required(('admin'), '/admin/login')
def category_delete_admin(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.warning(request, _("You have deleted category : " + category.title))
    return redirect('wishlist:category_list_admin')


@permission_required(('admin'), '/admin/login')
def category_revert_admin(request, item_id, history_id):
    category = get_object_or_404(Category, id=item_id)
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
def items_list(request):
    categories = Category.objects.annotate(num_items=Count('category_items')).filter(status='published')
    items = Item.objects.filter(status='published')

    return render(request, 'wishlist/front/items/list.html', {'categories': categories, 'items': items })


def item_detail(request, category_slug, item_slug):
    categories = Category.objects.annotate(num_items=Count('category_items')).filter(status='published')

    item = get_object_or_404(Item.objects.filter(
        category__slug=category_slug, slug=item_slug
    ).prefetch_related('participate'))

    form = BookItemForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            item = Item.objects.filter(slug=item_slug).first()
            item.participate.add(request.user)
            messages.success(request, _("You have successfully reserved : " + item.title))
            create_action(request.user, 'has book a gift', item)

            send_mail(_("Message from " + request.user.username + ': ' + request.user.email), form.cleaned_data['message'],
                      settings.DEFAULT_FROM_EMAIL, settings.EMAIL_RECIPIENTS)
            return redirect('wishlist:items_list_front')

    return render(request, 'wishlist/front/items/detail.html', {'categories': categories, 'item': item, 'form': form })

