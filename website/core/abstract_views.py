from django.views import View
from django.shortcuts import render, get_object_or_404
from .factory import AbstractFactory
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ugettext as _


class AbstractModelListView(View):
    model_class = None
    template = None

    def get(self, request):
        model_name = self.model_class.__name__.lower()
        model_name_plural = model_name + 's'
        models = self.model_class.admin.all()
        deleted_models = self.model_class.history.filter(history_type='-').order_by('-history_id')
        return render(request, self.template, {model_name_plural: models, 'deleted_' + model_name_plural : deleted_models})


class AbstractModelCreateView(View):
    template = None
    model_form_class = None
    category_form_class = None
    redirection_url = None

    def get(self, request):
        category_form = AbstractFactory.upsert(request, self.category_form_class)
        model_form = AbstractFactory.upsert(request, self.model_form_class)
        return render(request, self.template,
                      {'form': model_form, 'category_form': category_form, 'action': _("Create")})

    def post(self, request):
        category_form = AbstractFactory.upsert(request, self.category_form_class)
        model_form = AbstractFactory.upsert(request, self.model_form_class)
        if model_form.is_valid():
            messages.success(request, _("You have create ") + model_form.instance.__str__())
            return redirect(self.redirection_url)

        return render(request, self.template,
                      {'form': model_form, 'category_form': category_form, 'action': _("Create")})


def abstract_model_update(request, model_class, model_id, model_form_class, template, redirection_url, category_form_class=None):
    model = get_object_or_404(model_class, id=model_id)
    model_name = model_class.__name__.lower()
    model_name_plural = model_name + 's'
    model_form = AbstractFactory.upsert(request, model_form_class, model)
    category_form = AbstractFactory.upsert(request, category_form_class)
    if model_form.is_valid():
        messages.success(request, _("You have update : " + model_form.instance.__str__()))
        return redirect(redirection_url)

    historical_models = model.history.filter(id=model_id).order_by('-history_id')
    return render(request, template, {'form': model_form, 'category_form': category_form,
                                                         'historical_' + model_name_plural: historical_models,
                                                         'action': _("Update")})


def abstract_model_clone(request, model_class, model_id, model_form_class, template, redirection_url, category_form_class=None):
    model = get_object_or_404(model_class, id=model_id)
    model_form = AbstractFactory.upsert(request, model_form_class, model)
    category_form = AbstractFactory.upsert(request, category_form_class)
    if model_form.is_valid():
        messages.success(request, _("You have clone : " + model_form.instance.__str__()))
        return redirect(redirection_url)

    return render(request, template,
                  {'form': model_form, 'category_form': category_form, 'action': _("Clone")})


def abstract_model_revert(request, model_class, model_id, history_model_id, model_form_class, template, redirection_url, category_form_class=None):
    model = get_object_or_404(model_class, id=model_id)
    historical_model = model_class.history.get(history_id=history_model_id)
    model_form = AbstractFactory.upsert(request, model_form_class, model, historical_model)
    category_form = AbstractFactory.upsert(request, category_form_class)
    if model_form.is_valid():
        messages.success(request, _("You have revert post : " + model.__str__()))
        return redirect(redirection_url)

    return render(request, template,
                  {'form': model_form, 'category_form': category_form, 'action': _("Revert")})


def abstract_model_restore(request, model_class, history_model_id, model_form_class, template, redirection_url, category_form_class=None):
    historical_model = model_class.history.get(history_id=history_model_id)
    model_form = AbstractFactory.upsert(request, model_form_class, historical_model)
    category_form = AbstractFactory.upsert(request, category_form_class)
    if model_form.is_valid():
        historical_model.delete()
        messages.success(request, _("You have restore post : " + historical_model.__str__()))
        return redirect(redirection_url)

    return render(request, template, {'form': model_form, 'category_form': category_form, 'action': _("Restore")})


def abstract_model_delete(request, model_class, model_id, redirection_url):
    model = get_object_or_404(model_class, id=model_id)
    model.delete()
    messages.warning(request, _("You have deleted : " + model.__str__()))
    return redirect(redirection_url)