from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu Nombre'}
        ), min_length=3, max_length=100) #se usa label no verbose porque dentro del html crea un tag label
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu Email'}
        ), min_length=3, max_length=100) #NO OLVIDAR poner EmailInput sino quita la validacion previa de EmailFormat
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3, 'placeholder':'Escribe tu mensaje'}
        ), min_length=10, max_length=1000) #no se usa textfield, y widget para extender la conf de este campo