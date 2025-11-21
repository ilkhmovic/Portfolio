from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, AboutMe, Skill, Service, Portfel, SocialMedia, ContactMessage
from .forms import ContactForm

def home(request):
    category = Category.objects.all()
    about = AboutMe.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all().order_by("-created_at")
    portfels = Portfel.objects.all()
    socials = SocialMedia.objects.all()
    contact_info = ContactMessage.objects.filter(
        author_email__isnull=False
    ).order_by('-created_at').first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {
        'categories': category, 
        'about': about,
        'skills': skills,
        'services': services,
        'portfels': portfels,
        'socials': socials,
        'form': form,
        'contact_info': contact_info  
    })