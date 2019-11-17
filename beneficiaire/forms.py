from .models import Beneficiaire

class BeneficiaireForm(forms.ModelForm):
    class Meta:
        model = Beneficiaire
        fields = ('nom', 'prenom')
    )