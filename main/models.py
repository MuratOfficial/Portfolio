from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='project_images', blank=True)
    stack1 = models.CharField(max_length=64, default='')
    stack2 = models.CharField(max_length=64, default='')
    stack3 = models.CharField(max_length=64, default='')
    link_to_github = models.CharField(max_length=128, default='https://github.com')
    main_link = models.CharField(max_length=128, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

