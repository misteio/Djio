from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login, logout
from .forms import PasswordChangeCustomForm
from .services import ckupload_service
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from .utils import create_action
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.conf import settings
from django.utils.translation import ugettext as _


@permission_required(('admin'), '/admin/login')
def admin_password_change(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeCustomForm(request.user)
    return render(request, 'admin/auth/user/change_password.html', {
        'form': form
    })


@permission_required(('admin'), '/admin/login')
def ckeditor_upload(request):
    ckupload_service(request)


@permission_required(('admin'), '/admin/login')
def admin_editor_html(request):
    return render(request, 'admin/grapesjs.html')


def front_login(request):
    if request.user.is_active:
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Successful login.')
                    return redirect(settings.LOGIN_REDIRECT_URL)
                else:
                    messages.error(request, 'Account disabled.')
            else:
                messages.error(request, 'Login/password incorrect.')

    form = LoginForm()
    return render(request, 'front/users/login.html', {'form': form})


def front_logout(request):
    logout(request)
    return redirect('core:front_user_login')


def front_signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'front/users/signup.html', {'user_form': user_form})


@login_required(login_url='/login')
def front_edit_profile(request):
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
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'front/users/edit.html', {'user_form': user_form, 'profile_form': profile_form})
