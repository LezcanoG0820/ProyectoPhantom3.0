from django import forms
from .models import CustomUser  # Asegúrate de importar tu modelo CustomUser
from .models import GameCategory #Aqui importamos el modelo de vista de GameCategory

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'nombre']  # Asegúrate de agregar aquí el campo 'nombre'

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password) 
        if commit:
            user.save()
        return user
    
class GameCategoryForm(forms.ModelForm):
    class Meta:
        model = GameCategory
        fields = ['name', 'description']
        