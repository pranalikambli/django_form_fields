from django import forms
from django.forms import CharField, EmailField, MultiValueField


# creating a form
class FieldForm(forms.Form):
    name = forms.CharField(label='Enter Name', label_suffix=" : ", min_length=5, max_length=50,
                           empty_value='', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           help_text="Name length should be 50 character.",
                           error_messages={'required': "Please Enter your Name"}, disabled=False, strip=True)
    slug = forms.SlugField(label='Enter slug', label_suffix=" : ", empty_value='', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           help_text="Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                           error_messages={'required': "Please Enter slug"}, disabled=False)
    post_update = forms.DurationField(label='Enter post update duration', label_suffix=" : ",
                                      required=False, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                      help_text="Duration format should be(45:15:10)",
                                      error_messages={'required': "Please enter post update duration"}, disabled=False)
    loopback = forms.GenericIPAddressField(label='Enter Loopback IP Address', label_suffix=" : ", empty_value="",
                                           required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                           help_text="Loopback IP Address format should be(100.10.0.1)",
                                           protocol='IPv4', unpack_ipv4=False, disabled=False,
                                           error_messages={'required': "Please enter Loopback IP Address"})
    regex = forms.RegexField(label='Enter Regex', label_suffix=" : ", empty_value="", min_length=5, max_length=10,
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
