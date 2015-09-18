from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your models here.

class WeeblyUser(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    email = models.EmailField(blank=True)
    test_mode = models.BooleanField(default=True)
    language = models.TextField(default="en")

    def get_absolute_url(self):
        return reverse('user.detail.view', args=[str(self.id)])

    def __unicode__(self):
        return 'WeeblyUser ' + str(self.id)



