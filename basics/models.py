from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    summary = models.TextField()
    skills = models.TextField()
    softskills = models.TextField()
    language = models.TextField(null=True, blank=True)
    education = models.TextField(default="N/A",blank=True, null=True)
    start_year = models.CharField(max_length=10, blank=True, null=True)
    end_year = models.CharField(max_length=10, blank=True, null=True)
    cgpa = models.CharField(max_length=10, blank=True, null=True)
    company_one = models.CharField(max_length=200, blank=True, null=True)
    role_one = models.CharField(max_length=200, blank=True, null=True)
    job_one = models.TextField(blank=True, null=True)
    company_two = models.CharField(max_length=200, blank=True, null=True)
    role_two = models.CharField(max_length=200, blank=True, null=True)
    job_two = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Resume"
    

    
    