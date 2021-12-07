from django import forms
from .models import Profile,Comment

# class CreateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('user',profile_photo,'bio')
#         widgets = {'user':forms.OneToOneField(),}
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment        
        fields=['comment']
        
    