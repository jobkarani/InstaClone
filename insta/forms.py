from django import forms
from .models import Profile,Comment

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','profile_photo','bio')
        
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment        
        fields=['comment']
        
    