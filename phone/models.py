from django.db import models

# Create your models here.
class DamageReport(models.Model):
    title = models.CharField(max_length=255)
    broken_phone = models.ImageField(upload_to='uploads/phones/')

    def __str__(self):
        return self.title
