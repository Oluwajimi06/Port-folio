from django.db import models

# Create your models here.

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('front-end', 'Front-End'),
        ('development', 'Development'),
        ('e-commerce', 'E-commerce'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Choices for category
    tech_stack = models.CharField(max_length=255, default='N/A')  # Field for the tech stack
    link = models.URLField()
    date = models.DateField()  # Manually settable and editable

    def __str__(self):
        return self.title


