from django import forms
from django.forms import CharField, EmailField, MultiValueField


# creating a form
class FieldForm(forms.Form):
    name = forms.CharField(label='Enter Name', label_suffix=" : ", min_length=5, max_length=50,
                           required=False, disabled=False, strip=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           help_text="Name length should be 50 character.",
                           error_messages={'required': "Please Enter your Name"})
    slug = forms.SlugField(label='Enter slug', label_suffix=" : ", required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           help_text="Enter a valid slug consisting of letters, numbers, underscores or hyphens.",
                           error_messages={'required': "Please Enter slug"}, disabled=False)
    post_update = forms.DurationField(label='Enter post update duration', label_suffix=" : ",
                                      required=False, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                      help_text="Duration format should be(45:15:10)",
                                      error_messages={'required': "Please enter post update duration"}, disabled=False)
    loopback = forms.GenericIPAddressField(label='Enter Loopback IP Address', label_suffix=" : ",
                                           required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                           help_text="Loopback IP Address format should be(100.10.0.1)",
                                           protocol='IPv4', unpack_ipv4=False, disabled=False,
                                           error_messages={'required': "Please enter Loopback IP Address"})
    regex = forms.RegexField(label='Enter Regex', label_suffix=" : ", min_length=5, max_length=10,
                             regex=r'^[a-zA-Z0-9]+$',
                             required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
                             help_text="Regex format should be[a-z, A-Z, 0-9]", disabled=False,
                             error_messages={'required': "Please enter regex"})
    uuid = forms.UUIDField(label='Enter uuid', label_suffix=" : ", required=True, disabled=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           help_text="UUID format should be[123e4567-e89b-12d3-a456-426614174000]",
                           error_messages={'required': "Please enter uuid"})

    combo_field = forms.ComboField(label='Enter Email Id', label_suffix=" : ", required=True, disabled=False,
                                   fields=[CharField(max_length=20), EmailField()],
                                   widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   help_text="Pass valid email id with max length 20",
                                   error_messages={'required': "Please Email Id"})


class NumberFieldForm(forms.Form):
    Number = forms.IntegerField(label='Enter Number', label_suffix=" : ", min_value=1, max_value=100, required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 1 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Number."})
    rate = forms.FloatField(label='Rate Value', label_suffix=" : ", min_value=1, max_value=100, required=False,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}),
                            help_text="This value is greater than or equal to 1 & less than or equal to 100.",  disabled = False,
                            error_messages={'required': "Please Enter rate value."})
    fees = forms.DecimalField(label='Student Fees', label_suffix=" : ", min_value=1, max_value=100, max_digits=4,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=1, required=False,
                              help_text="This value is greater than or equal to 1 & less than or equal to 100. "
                                        "Also that there are no more than 4 digits in total.",
                              disabled = False,
                              error_messages={'required': "Please Enter Fees amount."})

class CheckBoxInputForm(forms.Form):
    is_valid = forms.BooleanField(label='Is Valid', label_suffix = " : ",
                                  required = True,  disabled = False,
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
                                  help_text = "Please check the box as this field is required.",
                                  error_messages = {'required':"Please check the box"})

class EmailInputForm(forms.Form):
    email= forms.EmailField(label='Enter Email ID', label_suffix = " : ",
                                  required = True,  disabled = False,
                                  widget=forms.EmailInput(attrs={'class': 'form-control'}),
                                  help_text = "Please provide a valid email Id.",
                                  error_messages = {'required':"Please provide valid email."})

class URLInputForm(forms.Form):
    url= forms.URLField(label='Enter URL', label_suffix = " : ",
                                  required = True,  disabled = False,
                                  widget=forms.URLInput(attrs={'class': 'form-control'}),
                                  help_text = "Please provide a valid URL.",
                                  error_messages = {'required':"Please provide valid URL."})

class NullBooleanForm(forms.Form):
    url= forms.NullBooleanField(label='Gender', label_suffix = " : ",
                                  required = True,  disabled = False,
                                  widget=forms.NullBooleanSelect(attrs={'class': 'form-control'}),
                                  help_text = "Select Gender.",
                                  error_messages = {'required':"This field is required."})