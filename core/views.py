import json
from django.shortcuts import render
from .models import Profile, Skill, Project, SocialLink, ContactInfo


def home(request):
    """Render the portfolio homepage with all dynamic content."""
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    socials = SocialLink.objects.all()
    contact = ContactInfo.objects.first()

    # Prepare typewriter roles as JSON for JavaScript consumption
    typewriter_roles = json.dumps(profile.get_typewriter_roles()) if profile else json.dumps([
        "Full Stack Developer", "Python Enthusiast", "Cloud Architect", "Software Engineer"
    ])

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'socials': socials,
        'contact': contact,
        'typewriter_roles': typewriter_roles,
    }
    return render(request, 'index.html', context)
