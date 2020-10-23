from django.urls import path

from . import views

urlpatterns = [
    path('text_input/', views.TextInputViews.as_view(), name="text_input"),
    path('number_input/', views.NumberInputViews.as_view(), name="number_input"),
    path('checkbox_input/', views.CheckBoxInputViews.as_view(), name="checkbox_input"),
    path('email_input/', views.EmailInputViews.as_view(), name="email_input"),
    path('url_input/', views.URLInputViews.as_view(), name="url_input"),
    path('null_boolean_input/', views.NullBooleanInputViews.as_view(), name="null_boolean_input"),
    path('select_input/', views.SelectInputViews.as_view(), name="select_input"),
    path('clearable_file_input/', views.ClearableFileInputViews.as_view(), name="clearable_file_input"),
    path('select_multiple_input/', views.SelectMultipleInputViews.as_view(), name="select_multiple_input"),
]