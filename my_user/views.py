from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from my_user.forms import LoginForm, MakeUser
from custom_user import settings

# Create your views here.
@login_required
def index(request):
    auth_value = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'auth_value':auth_value})


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'genericform.html', {'form': form})



def logged_outview(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))


def signup_view(request):
    if request.method == 'POST':
        form = MakeUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            create_user = MakeUser.objects.create_user(
                username=data['username'],
                password=data['password'],

            )

            create_user.save()
        return HttpResponseRedirect(reverse('login.html'))

    form = MakeUser()
    return render(request, 'signup.html', {'form': form})
