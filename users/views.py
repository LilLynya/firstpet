from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from users.forms import RegisterForm, AuthForm


# Create your views here.
def signup_page(request):
    if request.method == "POST":
        data_from_form = RegisterForm(request.POST)
        if data_from_form.is_valid():
            new_account = data_from_form.save(commit=False)
            new_account.set_password(data_from_form.cleaned_data['password'])
            new_account.save()
            return HttpResponseRedirect(reverse('workspace:workspace'))
    else:
        data_from_form = RegisterForm()

    data = {
        'register_data': data_from_form
    }
    return render(request, 'auth/signup.html', context=data)


class AuthView(LoginView):
    form_class = AuthForm
    template_name = 'auth/test.html'

    def get_success_url(self):
        return reverse_lazy('workspace:workspace')