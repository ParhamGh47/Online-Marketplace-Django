from django import forms
from .models import ConversationMessage

MESSAGE_INPUT_CLASS = (
    "w-full py-4 px-6 rounded-xl "
    "bg-[#0b0f14] text-gray-200 "
    "border border-teal-900 "
    "placeholder-gray-500 "
    "focus:outline-none focus:border-teal-500 "
    "focus:ring-2 focus:ring-teal-500/30 "
    "transition"
)

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': MESSAGE_INPUT_CLASS,
                'rows': 3,
                'placeholder': 'Type your message...'
            })
        }
