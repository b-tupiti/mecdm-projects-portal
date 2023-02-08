from django.forms import ModelForm
from django import forms
from .models import AccountRequest


class AccountRequestForm(ModelForm):
    class Meta:
        model = AccountRequest
        fields = [
            'username', 
            'email', 
            'first_name',
            'last_name',
            'occupation',
            'organization',
            'reason_for_request',
        ]
        widgets = {
          'reason_for_request': forms.Textarea(attrs={'rows':2,}),
        }
    
    def __init__(self, *args, **kwargs):
        super(AccountRequestForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'mb-2 form-control shadow-none rounded-1 border-0  border-secondary',
                'placeholder':field.label
                })
        