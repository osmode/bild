from PIL import Image, ImageStat, ImageDraw
from xremember.models import Xinput, Xresults, Imagedata 

from django.http import HttpResponse
from xremember.means import make_boxes, save_squares, fill_results_table
import numpy, os, dicom

#NOTE: the input file must be called "input.jpg" 
#and reside in inputimage folder
#NOTE: inputimage folder must be otherwise EMPTY!

def xdetect(request):
	output="Detect the lesion!"
	
	root='/home/osmode/aarann/bilder/xinputimage/'
	markedroot='/home/osmode/aarann/bilder/markedimage/'

	fileloopcounter=0

	for filename in os.listdir(root):
		outfile=os.path.splitext(filename)[0]+".cropped"
		if filename != outfile:

			ds=dicom.read_file(root+filename,force=True)
			xsize,ysize=ds.pixel_array.shape
			size=ds.pixel_array.shape
			pixarray=ds.pixel_array
			im=Image.frombuffer("I;16",size,ds.PixelData)

			#print "Dicom dataset: ",ds
			#print "Pixel data: ",ds.pixel_array
			#print "Dicom size: ",size

			pix=im.load()

			#returns a list of 4-tuples representing all the squares
			#in the grid
			boxes=[]
			boxes=make_boxes(32,32,xsize,ysize)
			print "boxes: ",boxes
			save_squares(boxes,pixarray,Xinput(),ds)

		fileloopcounter+=1

	stats=ImageStat.Stat(im)
	#get max and min values from cropping out bladder

	#initialize variables and lists
	match_scores=[]
	deviant_squares=[]
	running_total=0
	count=0
	std_dev=0

	#fills results table (xremember_xresults) with match id's
	#hits_list has 1024 nested lists containing matching id's
	#for each square
	hits_list=fill_results_table()

	#calculate match scores, and store them in 1024-element array
	for input_square in hits_list:
		for id_x in input_square:
			q=Xresults.objects.filter(result_id=id_x)
			count=q.count()
			running_total+=count
		#clear running_total in between lists
		match_scores.append(running_total)
		running_total=0
	
	#calculate standard deviation
	#note that match_scores has 1024 elements
	std_dev=numpy.std(match_scores)
	mean=numpy.mean(match_scores)
	print "match_scores: ",match_scores

	#print out all match scores
	#for score in match_scores:
		#print "match score: ",score
	
	print "Standard deviation: ",std_dev
	print "Mean: ",mean

	#if the match score of an input set is one std deviation or
	#more below the mean, label it as abnormal
	i=0
	for score in match_scores:
		if score < (mean-std_dev):
			#i refers to the square (0-1023)
			deviant_squares.append(i)
		i+=1
	
	print "Number of deviant squares: ",len(deviant_squares)

	#mark up the deviant squares and output the image
	im=make_jpeg(pixarray,size)
	marked_image=mark_image(im,deviant_squares,32,32)
	marked_image.save(markedroot+"input.marked","JPEG")
	
	return HttpResponse(output)

#function make_jpeg
def make_jpeg(pixdata_in,size_in):

	xsize,ysize=size_in

	im=Image.new('L',size_in)
	pix=im.load()

	maximum=pixdata_in.max()
	
	#convert 10-bit dicom image into new 8-bit jpeg
	correction_factor = (255.0/maximum)
	for i in range (xsize):
		for j in range (ysize):
			pix[i,j] = pixdata_in[i][j] * correction_factor
			print "jpeg pixel: ",pix[i,j]

	#im.save("/home/osmode/aarann/bilder/xinputimage/input.jpg","JPEG")
	return im
	
	

#function
#parameters: input image, square, number list, square dimensions
#(e.g. 32 rows x 32 columns grid)
#returns PIL image with marked outliers
def mark_image(image_in,square_num_list,num_rows,num_col):

	xsize,ysize=image_in.size
	square_width=xsize/num_col
	square_height=ysize/num_rows
	
	for square_num in square_num_list:
		x1=(square_num%num_rows)*square_width
		y1=(square_num/25)*square_height
		x2=x1+square_width
		y2=y1+square_height

		print "(x1,y1),(x2,y2)=(",x1,",",y1,"),(",x2,",",y2,")"

		box=(x1,y1,x2,y2)
		draw=ImageDraw.Draw(image_in)
		draw.rectangle(box, fill=128)
		#del draw

	return image_in



