from wishlist.models import Item as WishlistItem, Category as WishlistCategory
from page.models import Post as PagePost, Category as PageCategory
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType


class AbstractFactory():
    def upsert(request,form, item=None, historical_item=None):
        if request.method == 'POST':
            if item:
                if 'clone' in request.path:
                    abstract_form = form(data=request.POST)
                else:
                    abstract_form = form(data=request.POST, instance=item)
            else:
                abstract_form = form(data=request.POST)

            if abstract_form.is_valid():
                _post = abstract_form.save()
                _post.save()
            else:
                return abstract_form
        else:
            if item and historical_item:
                abstract_form = form(instance=historical_item)
            elif item:
                abstract_form = form(instance=item)
            else:
                abstract_form = form()

        return abstract_form


class MenuFactory():
    def upsert(request,form, item=None):
        if request.method == 'POST':
            if item:
                menu_form = form(data=request.POST, instance=item)
            else:
                menu_form = form(data=request.POST)

            if menu_form.is_valid():
                _menu = menu_form.save(commit=False)
                if 'class' in _menu.mapping:
                    _object_mapping=_menu.mapping.split(':')
                    _object = get_object_or_404(globals()[_object_mapping[1]], id=_object_mapping[2])
                    _menu.content_type = ContentType.objects.get_for_model(_object)
                    _menu.object_id = _object.id
                    _menu.save()

            else:
                return menu_form
        else:
            if item:
                menu_form = form(instance=item)
            else:
                menu_form = form()

        return menu_form