from django import forms

class Contact(forms.Form):
    name = forms.CharField(label = "Name", required=True, widget=forms.TextInput(
        attrs = {'class' : 'form-control'}
    ))
    mail = forms.EmailField(label = "Mail", required=True, widget=forms.EmailInput(
        attrs = {'class' : 'form-control'}
    ))
    subject = forms.CharField(label = "Subject", required=True, widget=forms.TextInput(
        attrs = {'class' : 'form-control'}
    ))
    message = forms.CharField(label = "Message", widget=forms.Textarea(
        attrs={'class':'form-control','rows' :3}
    ))