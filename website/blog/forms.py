from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import Post
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'title', 'author', 'slug')

    def __init__(self, *args, **kwargs):
        super(PostAdminForm, self).__init__(*args, **kwargs)

    checkboxes = forms.MultipleChoiceField(
        choices=(
            ('option_one', _('Option 1')),
            ('option_two', 'Option two can also be checked and included in form results'),
            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    appended_text = forms.CharField(
        help_text="Here's more help text"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
    )

    helper = FormHelper()
    helper.layout = Layout(
        HTML("""
            <div class="col-md-6">
                <div class="box box-info">
                    <div class="box-header with-border">
                        <h3 class="box-title">Text</h3>
                    </div>
                
                <div class="box-body">
        """),
        Field('body', rows="10", css_class='input-xlarge'),
        HTML("""
            </div></div></div>
            <div class="col-md-6"><div class="box box-success"><div class="box-header with-border">
            <h3 class="box-title">""" + _('Metadatas') + """</h3></div><div class="box-body">
        """),
        Field('title', css_class=''),
        Field('author'),
        Field('slug'),
        Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        AppendedText('appended_text', '.00'),
        PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">',
                      active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ),
        HTML("""
                </div> </div>
            """),
    )
