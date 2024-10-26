from django.db import models

class Main(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    banner_image = models.ImageField(upload_to='banners/')
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = ''
        