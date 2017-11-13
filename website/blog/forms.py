from django import forms
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import Post
from django.utils.translation import ugettext as _
from core.utils import open_box_form, close_box_form


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'title', 'author', 'slug', 'status')
        labels = {
            'body': _('Body of blog post'),
            'title': _('Title'),
            'author': _('Author'),
            'slug': _('Slug'),
            'status': _('Status'),
        }

    def __init__(self, *args, **kwargs):
        super(PostAdminForm, self).__init__(*args, **kwargs)

    helper = FormHelper()
    helper.layout = Layout(
        HTML(open_box_form('col-lg-9 col-md-12', _('Text of body'))),
        Field('body', rows="10", css_class='input-xlarge', id='body'),
        HTML(close_box_form() + open_box_form('col-lg-3 col-md-12', _('Metadatas'), 'box-success')),
        Field('title', css_class=''),
        Field('author'),
        Field('slug'),
        Field('status'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ),
        HTML("""
                </div> </div>
            """),
    )


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class LazyLoadAuthorManager(models.Manager):
    def get_queryset(self):
        return super(LazyLoadAuthorManager, self).get_queryset().select_related('author')