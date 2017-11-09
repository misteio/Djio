from django import forms
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import Item, Category
from django.utils.translation import ugettext as _
from core.utils import open_box_form, close_box_form


class ItemAdminForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('body', 'title', 'author', 'category', 'slug', 'status', 'url', 'image', 'price')
        labels = {
            'body': _('Body of Wishlist item'),
            'title': _('Title'),
            'category': _('Category'),
            'author': _('Author'),
            'slug': _('Slug'),
            'status': _('Status'),
            'url': _('URL of article'),
            'image': _('Image url'),
            'price': _('Price'),
        }

    def __init__(self, *args, **kwargs):
        super(ItemAdminForm, self).__init__(*args, **kwargs)

    helper = FormHelper()
    helper.layout = Layout(
        HTML(open_box_form('col-lg-9 col-md-12', _('Text of body'))),
        Field('body', rows="10", css_class='input-xlarge', id='body'),
        HTML(close_box_form() + open_box_form('col-lg-3 col-md-12', _('Metadatas'), 'box-success')),
        Field('title', css_class=''),
        Field('category'),
        Field('author'),
        Field('slug'),
        Field('status'),
        Field('url'),
        Field('image', id='image_input'),
        Field('price'),
        HTML("""
                <div class="row">
                    <div class="col-md-6">
                        <button class="btn btn-info" id="txtSelectedFile">Select a file</button>
                        <div id="modal-file" class="modais" data-izimodal-title="Select a file" data-izimodal-iframeURL="/admin/roxyfileman?integration=custom&type=files&txtFieldId=image_input"></div>
                    </div>
                    <div class="col-md-6">
                        <img id="image" src="" class="direct-chat-img" width="100px"> 
                    </div>
                    </br></br></br>
                </div>
                """),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ),
        HTML("""
                </div> </div>
            """),
    )


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description', 'slug', 'status')
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'slug': _('Slug'),
            'status': _('Status'),
        }

    def __init__(self, *args, **kwargs):
        super(CategoryAdminForm, self).__init__(*args, **kwargs)

    helper = FormHelper()
    helper.layout = Layout(
        HTML(open_box_form('col-lg-12 col-md-12', _('Name of Category'))),
        Field('title'),
        Field('slug'),
        Field('status'),
        Field('description'),

        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ),
        HTML("""
                </div> </div>
            """),
    )