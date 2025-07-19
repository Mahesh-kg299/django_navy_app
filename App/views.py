from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'App/home.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'App/register.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            return redirect('/app/register/')
        
        user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
        )
        user.set_password(password)
        user.save()
        return redirect('/app/login/')


class LoginView(View):
    def get(self, request):
        return render(request, 'App/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        if not User.objects.filter(username=username).exists():
            return redirect('/app/login/')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/app/')
        return redirect('/app/login/')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/app/login/')
        

class ShowAllView(LoginRequiredMixin, View):
    login_url = '/app/login/'
    def get(self, request, item):
        if item == 'ac':
            return render(request, 'App/allAircraftCarriers.html')
        elif item == 'ac_class':
            return render(request, 'App/allAircraftCarrierClasses.html')
        elif item == 'armament':
            return render(request, 'App/allArmaments.html')


class AddView(LoginRequiredMixin, View):
    login_url = "/app/login/"
    def get(self, request, item):
        if item == 'ac':
            return render(request, 'App/addAircraftCarrier.html')
        elif item == 'ac_class':
            return render(request, 'App/addAircraftCarrierClass.html')
        elif item == 'armament':
            return render(request, 'App/addArmament.html')

class SetArmamentView(LoginRequiredMixin, View):
    login_url = '/app/login/'
    def get(self, request):
        return render(request, 'App/setArmament.html')