from django import forms
from .models import Todos
from django.core.exceptions import ValidationError


class TodosForm(forms.ModelForm):


    def clean_title(self):
        title=self.cleaned_data["title"]
        print("title")
        
        if "@" in title:
            raise ValidationError("don't use @")
        return title


    class Meta:
        model = Todos
        fields = "__all__"