from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        
    content = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Write your message here ...."
    }))