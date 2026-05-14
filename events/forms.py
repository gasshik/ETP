from django import forms
from django_countries.widgets import CountrySelectWidget

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "location",
            "start_date",
            "event_country_flag",
            "end_date",
            "prize_pool",
            "event_type",
            "logo",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date", "class": "form_control"}),
            "end_date": forms.DateInput(attrs={"type": "date", "class": "form_control"}),
            "title": forms.TextInput(
                attrs={"class": "form_control", "placeholder": "Tournament Name"}
            ),
            "location": forms.TextInput(attrs={"class": "form_control", "placeholder": "Location"}),
            "prize_pool": forms.NumberInput(attrs={"class": "form_control"}),
            "event_type": forms.Select(attrs={"class": "form_select"}),
            "logo": forms.FileInput(attrs={"class": "form-control"}),
            "event_country_flag": CountrySelectWidget(attrs={"class": "form-select"}),
        }
