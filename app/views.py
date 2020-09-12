from django.views.generic import FormView

from .forms import FieldForm


class TextInputViews(FormView):
    template_name = 'text_input.html'
    form_class = FieldForm
    success_url = "/text_input"
