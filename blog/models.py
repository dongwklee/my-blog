from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()

	created_date = models.DateTimeField(default=timezone.now)
	picture = models.ImageField(upload_to='static/')
	published_date = models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class PostImage(models.Model):
	post = models.ForeignKey('Post', related_name='image_set')
	picture = models.ImageField(upload_to='static/')
