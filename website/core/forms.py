from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .utils import open_box_form, close_box_form, footer_form
from django.utils.translation import ugettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


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
        Field('username', css_class="form-control input-lg", placeholder="Username"),
        Field('password', css_class="form-control input-lg", placeholder="Password"),
        FormActions(
            Submit('save_changes', 'Sign In', css_class="btn btn-lg btn-success btn-block"),
        ),
        HTML("""
                    </div> </div>
                """),)