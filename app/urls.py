from django.urls import path

from . import views

urlpatterns = [
    path('text_input/', views.TextInputViews.as_view(), name="text_input"),
    path('number_input/', views.NumberInputViews.as_view(), name="number_input"),
]