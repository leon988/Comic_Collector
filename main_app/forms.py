# forms.py

from django.forms import ModelForm
from .models import Rating

class RatingForm(ModelForm):
  class Meta:
    model = Rating
    fields = ['date', 'rating']
