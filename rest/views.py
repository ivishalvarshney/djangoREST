from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# def index(request):
#     return HttpResponse("Hello, world. You're at the REST index.")

class users(APIView):
	"""This API is used to fetch the detail of heart rate of user"""
	def get(self, request):
		resp =[
			{"id":1,"firstname":"Antoine","lastname":"Kaufman","phone":"976842345"},
			{"id":2,"firstname":"Raphael","lastname":"Wallace","phone":"34564"},
		]
		return Response(resp)

	def put(self, request):
		resp =[
			{"id":1,"firstname":"Antoine","lastname":"Kaufman","phone":"976842345"},
			{"id":2,"firstname":"Raphael","lastname":"Wallace","phone":"34564"},
		]
		return Response(resp)