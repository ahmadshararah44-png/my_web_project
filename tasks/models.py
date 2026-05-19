from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Task Title")
    completed = models.BooleanField(default=False, verbose_name="Completed")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name="Priority")
    due_date = models.DateField(null=True, blank=True, verbose_name="Due Date")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title