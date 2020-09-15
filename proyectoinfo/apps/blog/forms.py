from django import forms

class NoticiaForm(forms.Form):
    titulo = forms.CharField()
    contenido = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass