import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
char_length = 128

class Category(models.Model): 
	name = models.CharField(max_length=char_length, unique=True)
	likes = models.IntegerField(default=0)
	views = models.IntegerField(default=0)
	slug = models.SlugField(blank=True)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
	class Meta:
		verbose_name_plural = 'categories'
	def __str__(self): 
		return self.name

class Page(models.Model): 
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	def __str__(self): 
		return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	def __str__(self):
		return self.user.username
