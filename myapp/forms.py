from django import forms  
from .models import Student,ImageModel

class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'age')


class ImageFrom(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']