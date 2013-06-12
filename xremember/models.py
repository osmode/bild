from django.db import models
from django.db import models

#imaging study is broken down into this many squares
SQUARES=1024
#temporary db table used for detection algorithm in xdetect.views
#purged in between used
class Xresults(models.Model):
	result_id=models.SmallIntegerField()

#model representing a cxr as a grid of SQUARES squares
#each image is represented as an instance

class Imagedata(models.Model):
	
	modality=models.CharField(max_length=100, null=True)
	#mean pixel values for the image x 'SQUARES' squares
	means=models.TextField()
	#'image' stores the image as a JPEG (no identifying data)
	#image=models.ImageField()

class Xinput(models.Model):

	modality=models.CharField(max_length=100, null=True)
	#mean pixel values for the image x 'SQUARES' squares
	means=models.TextField()
	#'image' stores the image as a JPEG (no identifying data)
	#image=models.ImageField()


