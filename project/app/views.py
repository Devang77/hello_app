from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class Hello(APIView):
    def get(self,request):
        return HttpResponse("Hello")
    def post(self,request):
        return HttpResponse("Hello")
