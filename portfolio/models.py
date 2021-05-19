from django.db import models
from ckeditor.fields import RichTextField

class	Heading(models.Model):
    	content = RichTextField()

class 	Project(models.Model):
	title=models.CharField(max_length=100)
	description=RichTextField()
	image=models.ImageField(upload_to='portfolio/images/')
	realeseddate=models.DateField()
	url=models.URLField(blank=True);

class 	Video(models.Model):
	caption=models.CharField(max_length=300)
	video= models.FileField(upload_to='video/')	
	def _str_(self):
		return self.caption
