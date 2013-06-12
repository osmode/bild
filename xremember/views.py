from PIL import Image
from PIL import ImageStat
from xremember.models import Imagedata, Xinput
import os, dicom

from django.http import HttpResponse
from xremember.means import make_boxes, save_squares


def remember_image(request):

	xsize=0
	ysize=0

	#try to open all jpegs in sourceimages
	#convert to 8-bit grayscale,
	#crop,  and save in DB
	#Note that no new images are saved in directory
	#and images are not altered

	fileloopcounter=0
	root='/home/osmode/aarann/bilder/xsourceimages/'
	for filename in os.listdir('/home/osmode/aarann/bilder/xsourceimages'):

		outfile=os.path.splitext(filename)[0]+".cropped"
		if filename != outfile:

			#try to open, in case a DICOM file
			ds=dicom.read_file(root+filename,force=True)
			
			#create new image
			
			xsize,ysize=ds.pixel_array.shape
			size=ds.pixel_array.shape
			pixarray=ds.pixel_array
			im=Image.frombuffer("I;16",size,ds.PixelData)

			print "Dicom dataset: ",ds
			print "Pixel data: ",ds.pixel_array
			print "Dicom size: ",size

			pix=im.load()

			boxes=[]
			boxes=make_boxes(32,32,xsize,ysize)
			save_squares(boxes,pixarray,Imagedata(),ds)

		fileloopcounter+=1
	
	
	return HttpResponse("Training complete with images in file 'sourceimages'")


