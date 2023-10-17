from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'h-32 w-full py-4 px-4 rounded-md border border-gray-300 focus:ring focus:ring-teal-500 focus:border-teal-500'
            })
        }