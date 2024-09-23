from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from .models import Project

app_name = 'sitepages'
def Home(request):
    projects = Project.objects.all()  # Fetch all projects

    if request.method == 'POST':
        # Contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            try:
                # Send the email
                send_mail(
                    subject=f"New Contact Form Submission: {subject}",
                    message=full_message,
                    from_email=email,  # Use the user's email as the from_email
                    recipient_list = [settings.EMAIL_HOST_USER],  # Your email to receive the message
                    fail_silently=False,
                )
                # Success message
                messages.success(request, 'Thank you for your message! I will get back to you soon.')
            except BadHeaderError:
                # Error in header
                messages.error(request, 'Invalid header found.')
        else:
            # Missing form fields
            messages.error(request, 'Please fill in all fields.')

    # Data for the projects and contact form
    data = {
        'ptitle': 'Obadimeji Oluwajimi',
        'projects': projects
    }

    return render(request, 'sitepages/index.html', data)


