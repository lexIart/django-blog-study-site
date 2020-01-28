from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):  # ModelForm inheritance makes our class more universal so we can change
                                 # page functional without any problems.
    # ModelForm also allowing to easily create/modify new objects so we don't need to realizing save method.
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    class Meta:
        model = Tag
        fields = ['title', 'slug']  # its better to explicitly list the fields we need that use __all.

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
    # title.widget.attrs.update({'class': 'form-control'})  define style for each input
    # slug.widget.attrs.update({'class': 'form-control'})   cause django generates html widgets

    def clean_slug(self):  # creating method that allow us to avoid the same tag names with case differences.
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be created with that name.')
        if Tag.objects.filter(slug__iexact=new_slug).count():  # unique tag checking method.
            raise ValidationError('Slug "{}" is already exists.'.format(new_slug))
        return new_slug

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be created with that name.')
        return new_slug