from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm


class Register_Form(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('blog-home')

    def get(self, request):
        form = UserCreationForm()
        template_name = 'users/register.html'
        return render(request, template_name, {'form': form})


class Profile_Form(View, LoginRequiredMixin):
    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        template_name = 'users/profile.html'
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }

        # def test_func(self):
        #     if self.request.user == u_form and self.request.user == p_form:
        #         return True
        #     return False
        return render(request, template_name, context)
