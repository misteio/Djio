from django import forms
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import Item, Category
from django.utils.translation import ugettext as _
from core.utils import open_box_form, close_box_form
from mptt.forms import TreeNodeChoiceField


class ItemAdminForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('body', 'title', 'author', 'category', 'slug', 'status', 'url', 'image', 'price', 'multi_participate')
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
            'multi_participate': _('Multi participate'),
        }

    def __init__(self, *args, **kwargs):
        super(ItemAdminForm, self).__init__(*args, **kwargs)

    category = TreeNodeChoiceField(queryset=Category.objects.all())
    helper = FormHelper()
    helper.layout = Layout(
        HTML(open_box_form('col-lg-9 col-md-12', _('Text of body'))),
        Field('body', rows="10", css_class='input-xlarge', id='body'),
        HTML(close_box_form() + open_box_form('col-lg-3 col-md-12', _('Metadatas'), 'box-success')),
        Field('title', css_class=''),
        HTML("""
               <div class="row">
                   <div class="col-md-6">

               """),
        Field('category', id="category_select"),
        HTML("""
                    </div>
                       <div class="col-md-6 btn-form-right">
                           <a href="#" onclick="return false;"  class="btn btn-success" id="categoryFormSelect">Create a Category</a>
                        </div>
                   </div>
                   """),
        Field('author'),
        Field('slug'),
        Field('status'),
        Field('url'),
        Field('multi_participate'),
        HTML("""
                   <div class="row">
                       <div class="col-md-6">

                   """),
        Field('image', id='image_input'),
        HTML("""
                </div>
                   <div class="col-md-6 btn-form-right">
                      <a href="#" onclick="return false;" class="btn btn-info" id="txtSelectedFile">Select a file</a>
                        <div id="modal-file" class="modais" data-izimodal-title="Select a file" data-izimodal-iframeURL="/admin/roxyfileman/?integration=custom&type=files&txtFieldId=image_input"></div>
                        <img id="image" src="" class="direct-chat-img" width="100px" style="margin-right:10px"> 
                    </div>
               </div>
               """),
        Field('price'),

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
        fields = ('title', 'description', 'slug', 'status', 'parent')
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'slug': _('Slug'),
            'status': _('Status'),
            'parent': _('Parent'),
        }

    def __init__(self, *args, **kwargs):
        super(CategoryAdminForm, self).__init__(*args, **kwargs)

    helper = FormHelper()
    helper.form_id = 'category-form'
    helper.layout = Layout(
        HTML(open_box_form('col-lg-12 col-md-12', _('Category'))),
        Field('title'),
        Field('slug'),
        Field('status'),
        Field('description'),
        Field('parent'),

        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ),
        HTML("""
                </div> </div>
            """),
    )


class BookItemForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':15}) )
    helper = FormHelper()
    helper.form_show_labels = False
    helper.layout = Layout(
        Field('message', css_class="form-control input-lg", placeholder=_('Write a message')),
        HTML('''
                   <p class="text-center">
                    <button type='submit' class="btn btn-template-main"><i class="fa fa-gift"></i> ''' + _('Make a gift') + '''</button>
                </p>
               '''),
    )