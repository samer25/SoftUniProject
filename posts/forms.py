from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs = {'class': 'textarea', }

    class Meta:
        model = Post
        exclude = ['created_by', 'date', ]
