from django.db import connection, transaction
from django.http import HttpResponse

#raw SQL queries to truncate database tables
def flush(request):
	
	cursor= connection.cursor()

	#data-modifying operation; commit required
	cursor.execute("truncate xremember_xresults")
	cursor.execute("truncate xremember_xinput")
	cursor.execute("truncate xremember_imagedata")
	#cursor.execute("truncate xremember_xinput")
	#cursor.execute("truncate xremember_xinput")
	#cursor.execute("truncate xremember_xinput")
	#cursor.execute("truncate xremember_xinput")

	#cursor.execute("truncate xremember_results, truncate xremember_xinput, truncate remember_results, truncate remember_input, truncate xremember_xinput");
	
	transaction.commit_unless_managed()
	
	output="Truncating databases..."

	return HttpResponse(output)

