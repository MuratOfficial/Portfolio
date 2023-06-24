from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='project_images', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

