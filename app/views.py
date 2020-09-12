from django.views.generic import FormView

from .forms import FieldForm, NumberFieldForm


class TextInputViews(FormView):
    template_name = 'text_input.html'
    form_class = FieldForm
    success_url = "/text_input"


class NumberInputViews(FormView):
    template_name = 'number_input.html'
    form_class = NumberFieldForm
    success_url = "/number_input"