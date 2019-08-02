from django.shortcuts import render, redirect
from sport.core.forms import EditProfileForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request, 'home.html')

def inscription(request):
	if request.method=="POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('succes')
	else:
		form = RegistrationForm()
	return render(request, 'registration/inscription.html', {
		'form':form
	})



def succes(request):
	return render(request, 'registration/signup_succes.html')



@login_required

def compte(request):
	return render(request, 'registration/compte.html')


def football(request):
	return render(request, 'registration/football.html')

def basketball(request):
	return render(request, 'registration/basketball.html')

def tenis(request):
	return render(request, 'registration/tenis.html')

def rugby(request):
	return render(request, 'registration/rugby.html')

def autres(request):
	return render(request, 'registration/autres.html')

def paris(request):
	return render(request, 'registration/paris.html')


def profile(request):
	form=EditProfileForm(request.POST, instance=request.user)
	return render(request, 'registration/profile.html', {
		'form':form
	})
	if request.method=="POST":
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('registration/compte.html')

	else:
		form=EditProfileForm(instance=request.user)
		args={'form': form}
		return render(request, 'registration/profile', args)