from django.db import models

# Create your models here.
def get_absolute_url(self):
    return reverse('accounts:login_view', args=[self.slug])
def get_absolute_url(self):
    return reverse('accounts:logout_view', args=[self.slug])
