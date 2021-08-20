from app.models import Contact
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import ContactMeForm

# Create your views here.
def home(request):
    return render(request,'index.html')

class ResumeContactView(CreateView):
    form_class = ContactMeForm
    template_name = 'index.html'
    success_url = '/'