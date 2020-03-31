# import re
# from django import forms
# from .models import Doctor
#
# NAME_CHOICES = [
#     ('mr','Mr.'),
#     ('mrs','Mrs.'),
# ]
# GENDER_CHOICES =[
#     ('iam','I am...'),
#     ('male','Male'),
#     ('female','Female'),
#     ('others','Others'),
# ]
# YEARS =[x for x in range(1940,2050)]
#
# class DoctorForm(forms.ModelForm):
#     # starting_name = forms.CharField(widget=forms.Select(choices=NAME_CHOICES))
#     full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=True, max_length=50)
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail'}),required=True , max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True, max_length=50)
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True, max_length=50)
#     dob = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
#     gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={'class':'form-control'}))
#     phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'tel'}), required=True, max_length=10)
#     address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':2,'cols':6}),required=True, max_length=1024)
#     hospital_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Hospital name'}), required=True, max_length=50)
#     zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'tel'}), required=True, max_length=6)
#
#
#     class Meta():
#         model = Doctor
#         fields = '__all__'
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
#         if email and not re.match(EMAIL_REGEX, email):
#             raise forms.ValidationError("Invalid Email")
#         return email
#
#     def clean_confirm_password(self):
#         pas = self.cleaned_data['password']
#         cpas = self.cleaned_data['confirm_password']
#         MIN_LENGTH = 8
#         if pas and cpas:
#             if pas != cpas:
#                 raise forms.ValidationError('Password does not match')
#             else:
#                 if len(pas) < MIN_LENGTH:
#                     raise forms.ValidationError('Password must be %d character!' % MIN_LENGTH)
#                 if pas.isdigit():
#                     raise forms.ValidationError('Password should not contain all numeric')
#
# class loginform(forms.ModelForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail'}),required=True , max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True, max_length=50)
#
#     class Meta():
#         model = Doctor
#         fields = ['email','password']
#
#
#
#
#
