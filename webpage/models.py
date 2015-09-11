from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Principal(models.Model):
    user_id = models.PositiveIntegerField(blank=True)
    email = models.EmailField()
    test_mode = models.BooleanField(default=True)
    language = models.TextField(default="en")


class weebly_site(models.Model):
    site_id = models.PositiveIntegerField(blank=True)
    domain_name = models.URLField()
    site_title = models.TextField(blank=True)
    brand_name = models.TextField(blank=True)
    brand_url = models.URLField(blank=True)
    upgrade_url = models.URLField(blank=True)
    publish_upsell_url = models.URLField(blank=True)
    allow_ssl = models.BooleanField(default=True)


class weebly_plan(models.Model):
    plan_id = models.PositiveIntegerField
    term = models.PositiveIntegerField(default=1) # one month




