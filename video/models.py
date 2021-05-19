from django.db import models

class Video(models.Model):
	caption=models.CharField(max_length=300)
	video= models.FileField(upload_to="video/%y")	
	def _str_(self):
		return self.caption
