from django.views.generic import FormView

from .forms import FieldForm, NumberFieldForm, CheckBoxInputForm, EmailInputForm, URLInputForm, NullBooleanForm


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


class URLInputViews(FormView):
    template_name = 'url_input.html'
    form_class = URLInputForm
    success_url = "/url_input"


class NullBooleanInputViews(FormView):
    template_name = 'null_boolean.html'
    form_class = NullBooleanForm
    success_url = "/null_boolean_input"