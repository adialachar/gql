from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from .models import Profile

class SignUpForm(UserCreationForm):
    class Meta:
      model = MyUser
      fields = (
         'email', 
         'password1', 
         'password2',
        )
    def save(self, commit=True):
        if self.cleaned_data.get('password1') == self.cleaned_data.get('password2') and self.cleaned_data.get('password1') and self.cleaned_data.get('password2'):
            if commit:
                u = MyUser.objects.create_user(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password2'))
                return u




class ProfileForm(forms.ModelForm):
   #learn or gain textfield is charfield with widget=forms.textarea in modelforms, min_length only in forms
   learn_or_gain = forms.CharField(min_length=250, widget=forms.Textarea, required=False)
   # BooleanField default blank is true hence only by setting required=True in forms.py will make it required 
   conduct_box = forms.BooleanField(required=True)
   share_box = forms.BooleanField(required=True)

   class Meta:
      model = Profile
      fields = (
	 'first_name',
   'last_name',
         'school', 
         'level_of_study', 
         'graduation_year',
         'major', 

         'gender',
	 'gender_other', 
         'date_of_birth',
         'race',
	 'race_other',
         'phone_number',
         'shirt_size',
         'dietary_restrictions',

         'linkedin', 
         'github', 
         'additional_link', 
         'description',
         'learn_or_gain',
         'resume',

         'conduct_box',
         'share_box',
      )
