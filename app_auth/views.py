from django.contrib import messages

from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy


def signupuser(request):
    if request.user.is_authenticated:
        return redirect('authors:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ви успішно зареєструвалися!')  # Додано повідомлення про успішну реєстрацію
            return redirect('quotes:main_quotes')
        else:
            return render(request, 'app_auth/registration.html', context={"form": form})

    return render(request, 'app_auth/registration.html', context={"form": RegisterForm()})



def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:main_quotes')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, "Username or password didn't match")
            return redirect(to='app_auth:login')

        login(request, user)
        return redirect(to='quotes:main_quotes')

    return render(request, 'app_auth/login.html', context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:main_quotes')
from django.shortcuts import render

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'app_auth/password_reset.html'
    email_template_name = 'app_auth/password_reset_email.html'
    html_email_template_name = 'app_auth/password_reset_email.html'
    success_url = reverse_lazy('app_auth:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'app_auth/password_reset_subject.txt'
