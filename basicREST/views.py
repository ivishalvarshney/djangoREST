from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import json
from django.http import QueryDict


def index(request):
    return HttpResponse("Hello, world. You're at the REST index.")

def get(request):
	if request.method == 'GET':
		value = request.GET.get('name', "blahblah")
		return HttpResponse("this is get request." + value)
	else:
		return HttpResponse("Invalid request.")

def post(request):
	if request.method == 'POST':
		value = str(request.POST.get('name', "blahblah"))
		return HttpResponse("this is POST request." + value)
	else:
		return HttpResponse("Invalid request.")

def put(request):
	if request.method == 'PUT':
		put = QueryDict(request.body)
		description = put.get('name')
		return HttpResponse("this is PUT request." + description)
	else:
		return HttpResponse("Invalid request.")

def delete(request):
	if request.method == 'DELETE':
		delete = QueryDict(request.body)
		description = delete.get('name')
		return HttpResponse("this is DELETE request." + description)
	else:
		return HttpResponse("Invalid request.")