from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=25)
    sport = models.CharField(max_length=30)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.username} : {self.sport}"