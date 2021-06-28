from django import forms
from .models import Post, Category, User

#choices = [('Coding', 'Coding'), ('Sports', 'Sports'), ('Entertainment', 'Entertainment')]
choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'snippet', 'body', 'header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control', 'value' : '', 'id' : 'user', 'type' : 'hidden'}),
            #'author' : forms.Select(attrs={'class' : 'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class' : 'form-control'})
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'snippet', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title_Tag'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the post here'}),
            'snippet' : forms.Textarea(attrs={'class' : 'form-control'})
        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
        }