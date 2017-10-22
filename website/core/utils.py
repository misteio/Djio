from django.utils.translation import ugettext as _


def open_box_form(div_class, title=None, box_class='box-primary'):
    if title:
        header = '<div class="box-header with-border"> <h3 class="box-title">' + title + '</h3> </div>'
        return '<div class="' + div_class +'"><div class="box ' + box_class + '"> ' + header + ' <div class="box-body">'
    else:
        return '<div class="' + div_class +'"><div class="box ' + box_class + '"><div class="box-body">'


def close_box_form():
    return '</div></div></div>'


def footer_form(text_cancel=_('Cancel'), text_submit=_('Submit')):
    return '<div class="box-footer"> <button type="reset" class="btn btn-default">' + text_cancel + '</button> <button type="submit" class="btn btn-info pull-right">' + text_submit +'</button> </div>'