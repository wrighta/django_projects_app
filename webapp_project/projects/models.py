from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
 

class Project(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1) 
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    stakeholders = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')],
        default='Pending'
    )
    image = models.ImageField(upload_to='', blank=True, null=True)  # No subfolder inside 'project_images'
    #image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.name
