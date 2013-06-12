from PIL import Image, ImageStat, ImageDraw
from xremember.models import Xinput, Xresults, Imagedata

from django.http import HttpResponse
from django.db import connection, transaction
from xremember.means import make_boxes,save_squares,fill_results_table
import numpy, os

#NOTE: the input file must be called "input.jpg" 
#and reside in inputimage folder
#NOTE: inputimage folder must be otherwise EMPTY!

def detect(request):

	output="Detect the lesion!"

	root='/home/osmode/aarann/bilder/inputimage/'
	markedroot='/home/osmode/aarann/bilder/markedimage/'
	fileloopcounter=0

	for filename in os.listdir(root):

		#flush databases before detection
		cursor = connection.cursor()
		cursor.execute("truncate xremember_xresults")
		cursor.execute("truncate xremember_xinput")
		transaction.commit_unless_managed()

		outfile=os.path.splitext(filename)[0]+".cropped"
		if filename != outfile:

			#convert image to 8-bit grayscale
			im=Image.open(root+filename)
			im=im.convert("L")
			pix=im.load()
			xsize,ysize=im.size
			size=im.size

			#in the grid
			boxes=[]
			boxes=make_boxes(32,32,xsize,ysize)
			#outfile=os.path.splitext(filename)[0]+".bladderless"
			#im.save(root+outfile,"JPEG")
			save_squares(boxes,pix,Xinput())


			#initialize variables and lists
			match_scores=[]
			deviant_squares=[]
			running_total=0
			count=0
			std_dev=0

			#fills results table (xremember_xresults) with match id's
			#hits_list has 1024 nexted lists containing matching id's
			#for each square
			hits_list = fill_results_table()

			#calculate match scores, and store them in 1024-element array
			for input_square in hits_list:
				for id_x in input_square:
					q=Xresults.objects.filter(result_id=id_x)
					
					count=q.count()
					running_total += count

				#clear running_total in between lists
				match_scores.append(running_total)
				running_total=0

			#calculate standard deviation
			#note that match_scores has 1024 elements
			std_dev=numpy.std(match_scores)
			mean=numpy.mean(match_scores)
			print "match_scores: ",match_scores

			#print out all match scores
			print "Standard deviation: ",std_dev
			print "Mean: ",mean

			#if the match score of an input is one std deviation or more
			#below the mean, label it as abnormal
			i=0
			for score in match_scores:
				if score < (mean-std_dev):
					deviant_squares.append(i)
				i+=1
			
	
			print "Number of deviant squares: ",len(deviant_squares)

			#mark up the deviant squares and output the image
			#note that the make_jpeg function is not called here 
			#(unlike in 'views.py' because image is already jpeg
			marked_image=mark_image(im,deviant_squares,32,32)
			output_name="input"+str(fileloopcounter)+".marked"
			marked_image.save(markedroot+output_name,"JPEG")


		fileloopcounter+=1

	return HttpResponse(output)

#function
#parameters: input PIL image (with bladder), square number list, square dimensions
#(e.g. 25 rows x 10 columns grid)
#returns image with marked outliers
def mark_image(image_in,square_num_list,num_rows,num_col):
	xsize,ysize=image_in.size
	square_width=xsize/num_col
	square_height=ysize/num_rows
	
	for square_num in square_num_list:
		x1=(square_num%num_rows)*square_width
		y1=(square_num/num_col)*square_height
		x2=x1+square_width
		y2=y1+square_height

		#print "(x1,y1),(x2,y2)=(",x1,",",y1,"),(",x2,",",y2,")"

		box=(x1,y1,x2,y2)
		draw=ImageDraw.Draw(image_in)
		draw.rectangle(box, fill=128)
		#del draw

	return image_in


