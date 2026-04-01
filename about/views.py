from django.contrib import messages
from django.shortcuts import render
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_page(request):
    """
    Display the about page.

    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, 'Collaboration request submitted successfully, I will endevour to respond within two days.')
            
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
    
    