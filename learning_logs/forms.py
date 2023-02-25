from django import forms
from  learning_logs.models import Topic , Entry  

class TopicForm(forms.ModelForm): 
    class Meta :
        model = Topic
        fields = ['text']
        widgets = {
            'text':forms.Textarea(attrs={'class': 'TopicForm'})
        }
        
        def __init__(self, *args, **kwargs):
            super(TopicForm, self).__init__(*args, **kwargs)
            self.fields['text'].required =False

    
class EntryForm(forms.ModelForm):
    class Meta : 
        model = Entry 
        fields = ['text']
        widgets = {
            'text':forms.Textarea(attrs={'class':'EntryForm'})
        }

   