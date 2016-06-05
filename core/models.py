from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Titulo(models.Model):
	descricao = models.CharField(max_length=60)
		
	def __str__(self):
		return self.descricao
			
	def get_absolute_url(self):
		return reverse('frmtitulos', kwargs={'pk': self.pk})