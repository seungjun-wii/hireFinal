from django import forms
from main.models import MyUser, UserInfo
from django.utils.translation import gettext_lazy as _

class UserForm(forms.Form):
    class Meta:
        model = MyUser
        fields = (
            "user_id",
            "password",
            "re_password",
            "name",
            "school",
            "date_of_birth",
        )

    user_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    school = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        if MyUser.objects.filter(user_id=self.cleaned_data['user_id']):
            raise forms.ValidationError('이미 사용 중인 아이디 입니다.')
        elif self.cleaned_data['password'] != self.cleaned_data['re_password']:
            raise forms.ValidationError('Check your password')

        return self.cleaned_data

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = (
            "intro",
            "skills",
            "experience",
            "initiatives"
        )