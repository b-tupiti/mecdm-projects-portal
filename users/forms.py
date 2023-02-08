from django.forms import ModelForm
from .models import UserProfile
        
        
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email','first_name', 'last_name',]

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'mb-2 form-control shadow-none rounded-1 border-0 bg-secondary border-secondary',})