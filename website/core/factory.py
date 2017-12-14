from django.contrib.contenttypes.models import ContentType
from .forms import UserEditForm, ProfileEditForm
from django.contrib import messages
from .models import Profile
from .utils import create_action
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _


class MenuFactory:
    def upsert(request, form, item=None):
        if request.method == 'POST':
            if item:
                menu_form = form(data=request.POST, instance=item)
            else:
                menu_form = form(data=request.POST)

            if menu_form.is_valid():
                _menu = menu_form.save(commit=False)
                if _menu.mapping:
                    if 'class' in _menu.mapping:
                        _object_mapping = _menu.mapping.split(':')
                        _object = get_object_or_404(globals()[_object_mapping[1]], id=_object_mapping[2])
                        _menu.content_type = ContentType.objects.get_for_model(_object)
                        _menu.object_id = _object.id
                        _menu.save()
                # If no menu mapping, we delete previous content type
                else:
                    _menu.content_type = None
                    _menu.object_id = None
                    _menu.save()
            else:
                return menu_form
        else:
            if item:
                menu_form = form(instance=item)
            else:
                menu_form = form()

        return menu_form


class UserFactory:
    def edit(request, template):
        if request.method == 'POST':
            user_form = UserEditForm(instance=request.user, data=request.POST)
            profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, _('Profile updated successfully'))
            else:
                messages.error(request, _('Error updating your profile'))
        else:
            user_form = UserEditForm(instance=request.user)
            if not hasattr(request.user, 'profile'):
                Profile.objects.create(user=request.user)
                create_action(request.user, 'has created a profile')

            profile_form = ProfileEditForm(instance=request.user.profile)

        return render(request, template, {'user_form': user_form, 'profile_form': profile_form})