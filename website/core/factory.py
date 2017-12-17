from django.contrib.contenttypes.models import ContentType
from .forms import UserEditForm, ProfileEditForm
from django.contrib import messages
from .models import Profile
from .utils import create_action
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from django.shortcuts import redirect


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
    def upsert(request, template, user_form_class=UserEditForm, profile_form_class=ProfileEditForm, user=None, action='update'):
        if not user:
            user = request.user
        else:
            #If we pass a user, it's not own profil update, so action become different
            current_user = request.user

        if request.method == 'POST':
            if action == 'update':
                user_form = user_form_class(instance=user, data=request.POST)
                profile_form = profile_form_class(instance=user.profile, data=request.POST, files=request.FILES)
            else:
                user_form = user_form_class(data=request.POST)
                profile_form = profile_form_class(data=request.POST, files=request.FILES)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                if action == 'update':
                    profile_form.save()
                    messages.success(request, _('Profile updated successfully'))
                    if not hasattr(user, 'profile'):
                        Profile.objects.create(user=user)
                        create_action(user, 'update profile')
                    if current_user:
                        return redirect('core:user_list_admin')
                else:
                    messages.success(request, _('User created successfully'))
                    profile = profile_form.save(commit=False)
                    profile.user = user_form.instance
                    profile.save()
                    create_action(request.user, 'has created a user', user)
                    return redirect('core:user_list_admin')
            else:
                messages.error(request, user_form.err)
        else:
            if action == 'update':
                user_form = user_form_class(instance=user)
                profile_form = profile_form_class(instance=user.profile)
            else:
                user_form = user_form_class()
                profile_form = profile_form_class()

        return render(request, template, {'user_form': user_form, 'profile_form': profile_form})