from django.db import models
from django.urls import reverse
from board.models import Board
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
    board=models.ForeignKey(Board,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=False,null=False)
    stage = models.CharField(max_length=4,
        choices=KANBAN_CHOICES,
        default=TODO,)


    date_created = models.DateField(auto_now=False,auto_now_add=True)

    def get_absolute_url(self):
        return reverse("cards:edit_view",kwargs={"id":self.id})
