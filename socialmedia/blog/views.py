from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

messages = [

	{
		'sender' : 'Ahmed',
		'message': 'you are bitch',	
	},

	{
		'sender' : 'Giorgii',
		'message': 'no you are bitch',	
	},

]

context = {
	'messages' : messages
}

def home(request):
	context['option'] = 1
	return render(request, 'blog/index.html', context)

def messages(request):
	context['option'] = 2
	return render(request, 'blog/messages.html', context)

def friends(request):
	context['option'] = 3
	return render(request, 'blog/index.html', context)

def groups(request):
	context['option'] = 4
	return render(request, 'blog/index.html', context)

def settings(request):
	context['option'] = 5
	return render(request, 'blog/index.html', context)