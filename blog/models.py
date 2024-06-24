from django.db import models
from django.utils import timezone
# Create your models here.
class Rasmlar(models.Model):
    nomi = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='rasm/images')
    def __str__(self):
        return self.nomi
class Matn(models.Model):
    nomi = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='rasm/images')
    text = models.TextField()
    chopetilish_vaqti = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-chopetilish_vaqti']
    object = models.Manager()

class Ishchilar(models.Model):
    rasm = models.ImageField(upload_to='rasm/images')
    ismi = models.CharField(max_length=200)
    kasbi = models.CharField(max_length=200)

    def __str__(self):
        return self.ismi


# Create your models here.

class Xodimlar(models.Model):
    rasm = models.ImageField(upload_to='rasm/images')
    ismi = models.CharField(max_length=200)
    kasbi = models.CharField(max_length=200)
    Text = models.TextField()

    def __str__(self):
        return self.ismi