from django.db import models

# Create your models here.

class Todos(models.Model):
    PRIORITY=[
        ("1", "high"),
        ("2", "medium"),
        ("3", "low"),
    ]
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_done=models.BooleanField(default=False)
    priority=models.CharField(max_length=50, choices=PRIORITY, default="3")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = ("Todos")