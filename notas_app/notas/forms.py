from django import forms
from .models import Nota


class NotaForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de productos.
    """

    class Meta: 
        #Espeficiar a que modelo está asociado el formulario
        model = Nota

        fields = [
            'titulo',
            'descripcion',
        ]

        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripción',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control','rows':4}),
        }
    
    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}