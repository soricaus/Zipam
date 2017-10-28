from django import forms


class ContactForm(forms.Form):
    nume = forms.CharField(label='Nume', required=True)
    telefon = forms.CharField(label='Telefon', required=False)
    oras = forms.CharField(label='Oras', required=True)
    email = forms.EmailField(label='Email', required=True)
    mesaj = forms.CharField(label='Mesaj', required=True, widget=forms.Textarea)

    def clean(self):
        data = self.cleaned_data
        return data
