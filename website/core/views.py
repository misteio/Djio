from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .forms import PasswordChangeCustomForm
from .services import ckupload_service
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import JsonResponse


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


