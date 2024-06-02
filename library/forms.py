from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    new_category = forms.CharField(required=True, label='分類')

    class Meta:
        model = Book
        fields = ['title', 'cover', 'pdf']

    def save(self, commit=True):
        new_category = self.cleaned_data.get('new_category')
        category, created = Category.objects.get_or_create(name=new_category)
        self.instance.category = category
        return super().save(commit=commit)
