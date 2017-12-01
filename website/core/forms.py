from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .utils import open_box_form, close_box_form, footer_form
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import Profile, Menu


class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)

        self.helper = FormHelper()
        self.helper.label_class = 'control-label'
        self.helper.layout = Layout(
            HTML(open_box_form('col-md-12')),
            'old_password',
            'new_password1',
            'new_password2',
            HTML(footer_form() + close_box_form()),
        )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_show_labels = False
    helper.layout = Layout(
        Field('username', css_class="form-control input-lg", placeholder=_("Username")),
        Field('password', css_class="form-control input-lg", placeholder=_("Password")),
        FormActions(
            Submit('save_changes', _('Sign in'), css_class="btn btn-lg btn-success btn-block"),
        ),
        )


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_show_labels = False
    helper.layout = Layout(
        HTML('''<div class="row"> '''),
        Field('username', css_class="form-control input-lg", placeholder=_('Username'), wrapper_class="col-md-12"),
        Field('email', css_class="form-control input-lg", placeholder=_('Email'), wrapper_class="col-md-12"),
        HTML(''' <div class= "col-xs-12 col-sm-6 col-md-6"> '''),
        Field('password', css_class="form-control input-lg", placeholder=_('Password')),
        HTML('''</div><div class= "col-xs-12 col-sm-6 col-md-6"> '''),
        Field('password2', css_class="form-control input-lg", placeholder=_('Repeat Password')),
        HTML(''' </div> </div> <div class="">
					 ''' + _('By clicking') + ''' <strong class="label label-success">''' +_('Signup') + '''</strong> , ''' + _('you agree to the Terms and Conditions set out by this site, including our Cookie Use.') + '''
                    </div><br/><hr class="colorgraph">
				'''),
        FormActions(
            Submit('save_changes', _('Signup'), css_class="btn btn-lg btn-success btn-block"),
        ),
    )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    helper = FormHelper()
    helper.form_tag = False
    helper.form_show_labels = False
    helper.layout = Layout(
        HTML('''<div class="row"> '''),
        Field('first_name', css_class="form-control input-lg", placeholder=_('Firstname'), wrapper_class="col-md-12"),
        Field('last_name', css_class="form-control input-lg", placeholder=_('Lastname'), wrapper_class="col-md-12"),
        Field('email', css_class="form-control input-lg", placeholder=_('Email'), wrapper_class="col-md-12"),
        HTML('''</div> '''),
        )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'zip_code', 'address', 'photo')

    helper = FormHelper()
    helper.form_tag = False
    helper.form_show_labels = False
    helper.layout = Layout(
        HTML('''<div class="row"> '''),
        Field('city', css_class="form-control input-lg", placeholder=_('City'), wrapper_class="col-md-12"),
        Field('zip_code', css_class="form-control input-lg", placeholder=_('ZipCode'), wrapper_class="col-md-12"),
        Field('address', css_class="form-control input-lg", placeholder=_('Address'), wrapper_class="col-md-12"),
        Field('photo', css_class="form-control input-lg", placeholder=_('Photo'), wrapper_class="col-md-12"),
        HTML('''</div> '''),
    )


class MenuAdminForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('title', 'url', 'mapping')
