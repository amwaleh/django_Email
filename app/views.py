from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def thankyou(request):

	
	# save_it = form.save(commit=false)
	# save_it.save()
	subject = 'thank you'
	message = 'welcome you been comp'
	from_email = settings.EMAIL_HOST_USER
	to_list =['alexmuturi@gmail.com','alex.mwaleh@andela.com']
	send_mail ( subject, message,from_email,to_list, fail_silently=False)
	messages.success(request,'Thank you')
	return HttpResponse("message sent")