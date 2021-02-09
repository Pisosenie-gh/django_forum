from django import forms

from .models import Zayavka


class ZayavkaForm(forms.ModelForm):
    """Форма Заявки"""

    class Meta:
        model = Zayavka
        fields = '__all__'