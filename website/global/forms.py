from django.contrib.auth.forms import PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML


class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)

        self.helper = FormHelper()
        self.helper.label_class = 'control-label'
        self.helper.layout = Layout(
            HTML("""
                    <div class="col-md-12">
                        <div class="box box-info">
                            <div class="box-header with-border">
                                <h3 class="box-title">Text</h3>
                            </div>

                        <div class="box-body">
                """),
            'old_password',
            'new_password1',
            'new_password2',
            HTML("""
                               <div class="box-footer">
                <button type="reset" class="btn btn-default">Cancel</button>
                <button type="submit" class="btn btn-info pull-right">Sign in</button>
              </div>
                           """),
        )