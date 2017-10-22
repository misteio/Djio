from django.contrib.auth.forms import PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML
from .utils import open_box_form, close_box_form, footer_form
from django.utils.translation import ugettext as _


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