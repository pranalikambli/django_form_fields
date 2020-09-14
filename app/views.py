from django.views.generic import FormView

from .forms import FieldForm, NumberFieldForm, CheckBoxInputForm, EmailInputForm


class TextInputViews(FormView):
    template_name = 'text_input.html'
    form_class = FieldForm
    success_url = "/text_input"


class NumberInputViews(FormView):
    template_name = 'number_input.html'
    form_class = NumberFieldForm
    success_url = "/number_input"


class CheckBoxInputViews(FormView):
    template_name = 'checkbox_input.html'
    form_class = CheckBoxInputForm
    success_url = "/checkbox_input"


class EmailInputViews(FormView):
    template_name = 'email_input.html'
    form_class = EmailInputForm
    success_url = "/email_input"