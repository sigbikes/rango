# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 17:01:15 2016

@author: Sig
"""
from django import forms
#from django.forms import ModelForm
from rango.models import Page, Category
from django.forms.widgets import TextInput


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length = 128, help_text = "Enter a Category Name.")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    slug = forms.CharField(widget = forms.HiddenInput(), required = False)

    #Inline class to return additional form information.
    class Meta:
        #Provide an association between ModelForm and Model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):

    title = forms.CharField(max_length = 128, help_text = "Enter a Page Title.")
    url = forms.URLField(max_length = 200, help_text = "Enter the Page URL.", widget = TextInput)
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 50)
    category = forms.ModelChoiceField(queryset = Category.objects.all(), help_text = "Select a Category.")

    #category_id =
    class Meta:
        #Provide an association between ModelForm and Model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        #exclude = ('category',)
        # or specify the fields to include (and thus exclude category)
        fields =  ('title', 'url', 'views', 'category')

    def clean(self):
        cleaned_data = self.cleaned_data
        #cleaned_data = super(PageForm,self).clean()
        url = cleaned_data.get('url')
        # Prepend 'http://' if not present and url not empty
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data
