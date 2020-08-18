from django import forms
from .models import Blog, Comment, Category

class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'

class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('commenter','text',)
        widgets = {
            'text': forms.Textarea(attrs={'class':'textarea'})
        }

class PostSearchForm(forms.Form):
    key_word = forms.CharField(
        label='キーワードや投稿者', required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    category = forms.ModelChoiceField(
        label='カテゴリの選択', required=False,
        queryset=Category.objects.all(),
    )
