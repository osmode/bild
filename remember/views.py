from PIL import Image
from PIL import ImageStat
from xremember.models import Imagedata, Xinput
import os

from django.http import HttpResponse
from xremember.means import make_boxes, save_squares

def remember_bonescans(request):

	#try to open all jpegs in sourceimages
	#convert to 8-bit grayscale,
	#crop, crop bladder, and save in DB
	#Note that no new images are saved in directory
	#and images are not altered

	xsize=0
	ysize=0

	fileloopcounter=0
	root='/home/osmode/aarann/bilder/sourceimages/'
	for filename in os.listdir(root):

		outfile=os.path.splitext(filename)[0]+".cropped"
		if filename != outfile:

			#convert image to 8-bit grayscale
			im=Image.open(root+filename)
			im=im.convert("L")
			#save black and white version
			#im.save(os.path.splitext(filename)[0]+".bw","JPEG")
			pix=im.load()
			xsize,ysize=im.size
			size=im.size

			#returns a list of 4-tuples representing all the squares
			#in the grid
			boxes=[]
			boxes=make_boxes(32,32,xsize,ysize)

			#compress and store in database
			save_squares(boxes,pix,Imagedata())

			#im.save(root+outfile,"JPEG")

		fileloopcounter+=1
	
	
	return HttpResponse("Training complete with images in file 'sourceimages'")



