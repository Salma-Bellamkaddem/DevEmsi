from django.forms import ModelForm,widgets
from .models import Project,Review
from django import forms




class projectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

        
    def __init__(self,*args,**kwargs):
        super(projectForm,self).__init__(*args,**kwargs)
        
        for name, value in self.fields.items():
            value.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
