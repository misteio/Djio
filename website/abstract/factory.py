class AbstractFactory:
    def upsert(request, form, item=None, historical_item=None):
        if request.method == 'POST':
            if item:
                if 'clone' in request.path:
                    abstract_form = form(data=request.POST)
                else:
                    abstract_form = form(data=request.POST, instance=item)
            else:
                abstract_form = form(data=request.POST)

            if abstract_form.is_valid():
                _model = abstract_form.save()
            else:
                return abstract_form
        else:
            if item and historical_item:
                abstract_form = form(instance=historical_item)
            elif item:
                abstract_form = form(instance=item)
            else:
                abstract_form = form()

        return abstract_form
