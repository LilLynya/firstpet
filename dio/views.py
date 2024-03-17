from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

# Forms
# from .forms import AuthForm, RegisterForm
from django.db.models import F

# Models

# Create your views here.
main_menu_buttons = [
    {"name": "Home", "link": '/'},
    {"name": "About Us", "link": '/info'},
    {"name": "Support", "link": '/support'},
]


def main_page(request):
    data = {
        'main_menu_buttons': main_menu_buttons
    }
    return render(request, 'main.html', context=data)


def about_us(request):
    data = {
        'main_menu_buttons': main_menu_buttons,
    }
    return render(request, 'about_us.html', context=data)

# @login_required
# def add_group(request):
#     if request.method == 'POST':
#         form = AddGroup(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AddGroup()
#     extra_context = {
#         'form': form
#     }
#     return render(request, 'addgroup.html', context=extra_context)


# def signup_page(request):
#     if request.method == "POST":
#         data_from_form = RegisterForm(request.POST)
#         if data_from_form.is_valid():
#             new_account = data_from_form.save(commit=False)
#             new_account.set_password(data_from_form.cleaned_data['password'])
#             new_account.save()
#             return reverse_lazy('workspace')
#     else:
#         data_from_form = RegisterForm()
#
#     data = {
#         'register_data': data_from_form
#     }
#     return render(request, 'auth/signup.html', context=data)
#
#
# class AuthView(LoginView):
#     form_class = AuthForm
#     template_name = 'auth/login.html'
#
#     # def get_success_url(self):
#     #     url_match = reverse_lazy('workspace')
#     #     return redirect(url_match)
#
#     def form_valid(self):
#         return redirect('workspace')

# @login_required
# def make_a_task(request):
#     if request.method == 'POST':
#         data_from_form = Task(request.POST)
#         if data_from_form.is_valid():
#             task = data_from_form.save(commit=False)
#             role = get_user_model().objects.filter(username = F(request.user.username))
#             task.save(by=request.user.username,  )
#             return redirect('workspace')
#     else:
#         data_from_form = Task()
#     extra_context = {
#         'form': data_from_form,
#     }
#     return render(request,'task.html', context=extra_context)
