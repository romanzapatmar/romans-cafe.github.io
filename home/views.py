from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages #to display a message after form submit
# Create your views here.
def index(request):
    # return HttpResponse('This is HomePage')
    context = {
        'var1': 'This is variable value',
        'var2': 'This is var2 value'
    } #set of variables
    return render(request, 'index.html', context) #use render if you want to renedr a template file

#about page
def about(request):
    # return HttpResponse('This is About Page')
    return render(request, 'about.html')

#services page
def services(request):
    # return HttpResponse('This is Services Page')
    return render(request, 'services.html')

#contact page
def contact(request):
    # return HttpResponse('This is Contact Page')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')
        contact = Contact(name=name, email=email, phone=phone, comments=comments, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')
