from django.utils.translation import ugettext as _
from .models import Action
import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from wishlist.models import Item, Category as WishlistCategory
from page.models import Post as PagePost, Category as PageCategory
from constance import config


def open_box_form(div_class, title=None, box_class='box-primary'):
    if title:
        header = '<div class="box-header with-border"> <h3 class="box-title">' + title + '</h3> </div>'
        return '<div class="' + div_class +'"><div class="box ' + box_class + '"> ' + header + ' <div class="box-body">'
    else:
        return '<div class="' + div_class +'"><div class="box ' + box_class + '"><div class="box-body">'


def close_box_form():
    return '</div></div></div>'


def footer_form(text_cancel=_('Cancel'), text_submit=_('Submit')):
    return '<div class="box-footer"> <button type="reset" class="btn btn-default">' + text_cancel + '</button> <button type="submit" class="btn btn-info pull-right">' + text_submit +'</button> </div>'


def create_action(user, verb, target=None):
    # check for any similar action made in the last minute
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user_id=user.id,
                                            verb=verb,
                                            created_at__gte=last_minute)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct,
                                                 target_id=target.id)

    if not similar_actions:
        # no existing actions found
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False


def links_for_menu_items():
    html = '<optgroup label="' + _('Pages') + '">'
    page_posts = PagePost.objects.select_related('author').all()
    for page_post in page_posts:
        html += "<option value='class:wishlist:" + str(page_post.id) + "'>" + page_post.title + "</option>"
    html += '</optgroup>'
    html += '<optgroup label="' + _('Page Categories') + '">'
    page_categories = PageCategory.objects.all()
    for page_category in page_categories:
        html += '<option value>' + page_category.title + '</option>'
    html += '</optgroup>'


    if(config.MODULE_WISHLIST):
        html += '<optgroup label="' + _('Wishlist') + '">'
        wishlists = Item.admin_load.all()
        for wishlist in wishlists:
            html += '<option value>' + wishlist.title + '</option>'
        html += '</optgroup>'

        html += '<optgroup label="' + _('Wishlist Categories') + '">'
        wishlist_categories = WishlistCategory.objects.all()
        for wishlist_category in wishlist_categories:
            html += '<option value>' + wishlist_category.title + '</option>'
        html += '</optgroup>'

    return html