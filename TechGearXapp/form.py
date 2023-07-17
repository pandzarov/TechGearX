from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from TechGearXapp.models import Post


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        if commit:
            user.save()

        return user


class PostForm(forms.ModelForm):
    def __init__(self, *arg, **kwargs):
        super(PostForm, self).__init__(*arg, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = Post
        exclude = ("author",)
        fields = ['title', 'category', 'price', 'image']
