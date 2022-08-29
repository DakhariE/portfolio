from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail

# Create your views here.

def index(request):
  projects = Project.objects.all()
  if request.method == "POST":
    contact_name = request.POST['contact-name']
    contact_email = request.POST['contact-email']
    contact_text = request.POST['contact-text']

    send_mail(
      "Message from, " + contact_name,
      f"From: {contact_email} \nMessage: \n{contact_text}",
      contact_email ,
      ["piratedevil72@gmail.com"],
    )
    
    return render(request, 'index.html', {'contact_name': contact_name,'projects': projects})

  else:
    return render(request, 'index.html', {'projects': projects})

