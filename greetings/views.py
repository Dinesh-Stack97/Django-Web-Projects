from django.shortcuts import render

from django.http import HttpResponse

import datetime

# Create your views here.
#function based view

def welcome_clients(request):
	date = datetime.datetime.now()
	msg1 = '<h1>Welcome Clients</h1>'

	#The type of date is object
    
	msg2 ='<marque>' +msg1 + '<h1>The current server time is:' + str(date) + '</h1> </marque>'

	return HttpResponse(msg2)
