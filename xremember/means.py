#from __future__ import division
from PIL import Image
from PIL import ImageStat
from xremember.models import Imagedata, Xinput, Xresults
from django.db import connection,transaction
import numpy

#MARGIN_OF_ERROR is the permissible difference in mean
#square values between input and repository values
MARGIN_OF_ERROR=1

#function make_boxes populates a list of 4-tuples
#each representing a cols x rows grid
#xsize and ysize represent the dimensions of the image
def make_boxes(rows, cols, xsize, ysize):
	x_increment=xsize/cols
	y_increment=ysize/rows

	boxes=[]
	i=0
	j=0

	while i<rows:
		while j<cols:

			left=(j*x_increment)
			right=left+x_increment
			top=(i*y_increment)
			bottom=top+y_increment
			box=(left,top,right,bottom)
			boxes.append(box)
			
			j+=1
		i+=1
		j=0
	
	return boxes

	
#function save_squares saves the means of all the squares
#in the DB
#parameter squares_in is a list containing 4-tuples representing
#all the squares
#paramter image_in is an Image instance
#paramter class_in is the db table and model class
#dicom is a boolean value indicating if the pixel data is from a dicom file
#or not
def save_squares(squares_in,image_in,class_in, dicom_in=False):
	#values is a list storing all 1024 values
	values=[]
	means=[]
	string=''

	#for each box in the squares_in list
	for four_tuple in squares_in:
		top,left,bottom,right=four_tuple

		print "four_tuple: ", four_tuple
		
		#traverse rows 'top' to 'bottom' (including bottom)
		#and colummns 'left' to 'right' (including right)
		#adding all the means
		i=top
		j=left
		while i< (bottom):
			while j< (right):
				#store of pixel data varies depending on 
				#whether a dicom file was passed or not
				if dicom_in:
					values.append(image_in[i][j])
				else:
					values.append(image_in[i,j])

				j+=1
			i+=1

		#find the mean of list 'values' for each square
		#and append to list 'means'
		mean=numpy.mean(values)
		means.append(mean)
		values=[]
		
		print "mean for square: ", mean	
	
	#for each mean (each square has one mean), convert
	#into string
	for this_mean in means:
		this_mean=int(this_mean)
		string+=str(this_mean)+'.'
	
	#and save in the 'means' column in the corresponding
	#db table
		
	q=class_in
	q.means=string

	#if a dicom file was passed as argument, store modality in DB
	if(dicom_in):
		q.modality=str(dicom_in.Modality)

	print "string: ",string

	#save jpeg image data in database as PIL image
	#q.image=image_in
	q.save()


def fill_results_table():

	#uniques_list is a list that stores lists of id's
	#it is returned at the end
	#and is used in xdetect.views 
	#temp_list holds id values from each set
	hits_list=[]
	temp_list=[]
	#holds all means from xremember_imagedata
	means_repository_list=[]

	#get the first row in the xremember_xinput table
	q=Xinput.objects.get(pk=1)
	means_string=q.means
	#means_list contains means from input image
	means_list=means_string.split(".")
	#convert to integers
	for mean in means_list:
		if mean=='':
			means_list.remove(mean)
		elif mean:
			mean=int(mean)
		

	#print "means_list: ",means_list

	#NOTE: primary key 'id' in xremember_imagedata
	#must correspond to variable 'primary_key_counter'

	#create two-dimensional list containing
	#mean values extracted from xremember_imagedata table
	results=Imagedata.objects.all()
	#for each row in the xremember_imagedata table...
	for result in results:
		temp_means_string=result.means
		temp_means_list=temp_means_string.split(".")
		for mean in temp_means_list:
			if mean=='':
				temp_means_list.remove(mean)
			elif mean:
				mean=int(mean)


		means_repository_list.append(temp_means_list)
		temp_means_list=[]
	
	#print "means_repository_list: ",means_repository_list	
	#get all images whose square value
	#is equal to the input image, +/- margin of error
	primary_key_counter=1
	#for each square in the input image (i.e. 1024)
	for index,value in enumerate(means_list):
		#for each row in the xremember_imagedata tbl
		for row in means_repository_list:
		
			#compare input value and db value
			#at corresponding index
			#if ~equal, add the index to the 
			#temp list (index==primary key)
			a=int(row[index])
			b=int(means_list[index])

			if abs(a - b) <MARGIN_OF_ERROR:
				#print "new match id: ",primary_key_counter
				new_result=Xresults(result_id=primary_key_counter)
				new_result.save()

				#temp_list contains all id matches
				#for each iteration corresponding to a square
				temp_list.append(primary_key_counter)
		
			primary_key_counter+=1
		#after each iteration through the entire xremember_imagedata database 
		#(which occurs once per square = 1024 times)
		#add the list of id's to hits_list
		#and clear temp_list
		#and reset primary_key_counter to 1
		#hits list will have 1024 nested lists
		hits_list.append(temp_list)
		temp_list=[]
		primary_key_counter=1
	
				
	print "hits_list: ",hits_list

	return hits_list


