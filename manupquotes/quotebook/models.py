from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quote(models.Model):
    class Meta:
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.quote[0:50] + ' - ' + self.author

    author = models.CharField(max_length=255, blank=False, null=False)
    quote = models.TextField(blank=False, null=False)
    owner = models.ForeignKey(User, 
            blank=False, null=False, 
            related_name='quotes', help_text="The user that submitted this quote",
            on_delete=models.DO_NOTHING)
    background = models.ImageField(upload_to="backgrounds/")
