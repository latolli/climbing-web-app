from django import forms

class AddTraining(forms.Form):
    date = forms.DateField()

class AddClimb(forms.Form):
    date = forms.DateField()
    grade = forms.IntegerField()