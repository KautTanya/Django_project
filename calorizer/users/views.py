from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm, UserProfileForm, PhoneNumberFormSet


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        phone_formset = PhoneNumberFormSet(request.POST, prefix='phone_numbers')

        if user_form.is_valid() and profile_form.is_valid() and phone_formset.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            phone_formset.instance = profile
            phone_formset.save()

            login(request, user)
            return redirect('registration_success')
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()
        phone_formset = PhoneNumberFormSet()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'phone_formset': phone_formset,
    }
    return render(request, 'users/register.html', context)


def registration_success(request):
    return render(request, 'users/registration_success.html')

