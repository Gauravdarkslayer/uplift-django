from django import forms

class CreateBlog(forms.Form):
    title = forms.CharField(label='Blog Title', max_length=100)
    description = forms.CharField(label='Blog Description', max_length=100)

    