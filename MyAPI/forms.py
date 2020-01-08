from django import forms

class ApprovalForm(forms.Form):
    Question = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter how many questions'}))
    Clearmarks = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter clearing marks'}))
    Obtainmarks = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter obtain marks'}))
    Time = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter how much time it take to solve questions'}))

