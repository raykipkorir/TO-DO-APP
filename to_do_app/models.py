from django.db import models
from django.urls import reverse


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("update_task", kwargs={"pk": self.pk})
    

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
