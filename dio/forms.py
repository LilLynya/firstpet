from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


# Models


# class AuthForm(AuthenticationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'password']
#         labels = {
#             'username': 'Enter your login',
#             'password': 'Enter your password'
#         }
#
#     # def clean_password(self):
#     #     user_password = self.cleaned_data['password']
#     #
#     #     if get_user_model().objects.filter(password = user_password) != user_password:
#     #         raise forms.ValidationError("You entered incorrect password or this account doesn't exist")
#     #     return user_password
#
#
# class RegisterForm(forms.ModelForm):
#     username = forms.CharField(min_length=3)
#     password = forms.CharField(widget=forms.PasswordInput,
#                                min_length=8,
#                                error_messages={'password': "Your password must contains at least 8 characters.", },
#                                label='Enter your password')
#     password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat your password")
#     group_id = forms.CharField(required=False)
#     role = forms.ChoiceField(choices=(('trainee', 'Trainee'),
#                                       ('project_manager', 'Project Manager'),
#                                       ('developer', 'Developer'),))
#
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
#         labels = {
#             'username': 'Enter your nickname',
#             'email': 'Enter your email',
#             'password': 'Enter your password',
#             'first_name': 'Enter your name',
#             'last_name': 'Enter your surname',
#             # 'group_id': 'Specify the number of group(This form maybe null)',
#         }
#
#     def clean_password2(self):
#         clean_data = self.cleaned_data
#         if clean_data['password'] != clean_data['password2']:
#             raise forms.ValidationError("Passwords don't match")
#         else:
#             return clean_data['password']
#
#     def clean_email(self):
#         user_email = self.cleaned_data['email']
#         if get_user_model().objects.filter(email=user_email).exists():
#             raise forms.ValidationError("This email already exists")
#         else:
#             return user_email

# class AddGroup(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['group_id']
#         labels = {
#             'group_id': 'Specify number of your group'
#         }
