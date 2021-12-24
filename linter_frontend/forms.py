from django import forms
from django.db.models import TextChoices

class LinterForm(forms.Form):
    class MoocChoices(TextChoices):
        MOOC38 = "https://mooc38.escolavirtual.gov.br/login/index.php"
    
    moodle_login_url = forms.ChoiceField(choices=MoocChoices.choices, label="Moodle URL")
    moodle_course_url = forms.URLField(label="Moodle Course URL")
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
