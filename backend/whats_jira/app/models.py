from django.db import models

# Create your models here.
class JiraTicket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    issue_type_id = models.CharField(max_length=10, default="10003")  
    priority_id = models.CharField(max_length=10, default="3")  
    labels = models.JSONField(default=list)  
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title