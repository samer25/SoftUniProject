from django import forms

from posts.models import Post, CommentPostModel


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs = {'class': 'textarea', }

    class Meta:
        model = Post
        exclude = ['created_by', 'date', 'likes']


class CommentPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentPostForm, self).__init__(*args, **kwargs)
        self.fields['comments'].widget.attrs = {'class': 'comments_text_area', }

    class Meta:
        model = CommentPostModel
        exclude = ['post', 'date', 'user_comm']
