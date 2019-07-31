from django.db import models
from django.urls import reverse
# Create your models here.

class Card(models.Model):
    TODO = 'todo'
    IN_PROGRESS = 'inpr'
    DONE = 'done'
    KANBAN_CHOICES = [
        (TODO, "To-Do"),
        (IN_PROGRESS, "In-Progress"),
        (DONE, "Done")
    ]

    title = models.CharField(max_length=50)
    description = models.TextField(blank=False,null=False)
    stage = models.CharField(max_length=4,
        choices=KANBAN_CHOICES,
        default=TODO,)


    date_created = models.DateField(auto_now=False,auto_now_add=True)

    def get_absolute_url(self):
        return reverse("card:card",kwargs={"card_id":self.id})
