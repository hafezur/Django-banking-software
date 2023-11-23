from django.shortcuts import render,redirect
from django.views.generic import FormView # different view exist in django.
from.forms import UserRegistrationForm
from django.contrib.auth import login ,logout
# Create your views here.

from django.urls import reverse_lazy
class UserRegistrationViews(FormView):
    template_name='accounts/user_registration.html' # no need to add templates directly rether then templates containing folder must added because templates is keyword in django.
    form_class=UserRegistrationForm # this is one kind of form.
    success_url=reverse_lazy('register') # reverse_lazy is used for  quick reload for webpage. # where is from register? ans--> register is from url name, for more check app urls.py
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user=form.save() # user ar data database a save hossa.
        login(self.request,user) # user login hossa.
        print(user)
        return super().form_valid(form) # for super keyword form_valid function call itself.


from django.contrib.auth.views import LoginView # come from class based view.
class UserLoginView(LoginView):
    template_name='accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home') # this 'home' come from sunrise bank project urls. see there.


from django.contrib.auth.views import LogoutView # come from class based view.
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')



from .forms import UserUpdateForm
from django.views import View # come from class based view.
class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form}) 