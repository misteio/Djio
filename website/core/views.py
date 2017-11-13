from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login, logout
from .forms import PasswordChangeCustomForm
from .services import ckupload_service
from .forms import LoginForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


@permission_required(('admin'), '/admin/login')
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
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
def editor_html(request):
    return render(request, 'admin/grapesjs.html')


def front_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                print('error')

    form = LoginForm()
    return render(request, 'front/users/login.html', {'form': form})


def front_signup(request):
    return render(request, 'front/users/login.html')


