from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

messages = [

	{
		'sender' : 'Ahmed',
		'message': 'Hello Giorgii, how are u doing?',	
	},

	{
		'sender' : 'Giorgii',
		'message': 'Hi, bro, I am fine, what about u?',	
	},

]

context = {
	'messagesUser' : messages
}

@login_required
def home(request):
	context['option'] = 1
	return render(request, 'blog/home.html', context)

@login_required
def messages(request):
	context['option'] = 2
	return render(request, 'blog/messages.html', context)

@login_required
def friends(request):
	context['option'] = 3
	return render(request, 'blog/index.html', context)

@login_required
def groups(request):
	context['option'] = 4
	return render(request, 'blog/index.html', context)

@login_required
def settings(request):
	context['option'] = 5
	return render(request, 'blog/index.html', context)