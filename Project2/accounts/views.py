from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from  .forms import UserRegistrationForm
from .models import User   

# Create your views here.
class signupView(CreateView):
    model =User
    form_class =UserRegistrationForm
    template_name = "products/forms/form.html"
    extra_context ={
        "form_title" : "Sign Up "
    }
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        print(self.request.FILES)  # for depugging 
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)