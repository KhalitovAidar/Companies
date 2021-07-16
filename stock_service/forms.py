from django import forms


class CompanyForm(forms.Form):
    company = forms.CharField(label='Your name', max_length=100)
