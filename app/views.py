from django.views.generic import FormView

from .forms import *


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


class SelectInputViews(FormView):
    template_name = 'select_input.html'
    form_class = SelectInputForm
    success_url = "/select_input"


class ClearableFileInputViews(FormView):
    template_name = 'clearable_file_input.html'
    form_class = ClearableFileInputForm
    success_url = "/clearable_file_input"


class SelectMultipleInputViews(FormView):
    template_name = 'select_multiple_input.html'
    form_class = SelectMultipleForm
    success_url = "/select_multiple_input"