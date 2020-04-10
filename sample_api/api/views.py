# from django.shortcuts import render
# from django.http import HttpResponse
# import json
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from api import serializers,models
import io 
import json

# Create your views here.
# @api_view()
# def usersApi(request):
#     users = [
#         {
#             "name" : "Yash Gupta",
#             "language" : "C++"
#         },
#         {
#             "name" : "Prateek",
#             "language" : "Python"
#         }
#     ]
#     # return HttpResponse(json.dumps(users))
#     return Response(users)
#  Using serializers
class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
@api_view()
def usersApi(request):
    student1 = Student("Yash",1,100)
    student2 = Student("Karan",2,99)
    student3 = Student("Avinash",3,98)
    response = serializers.StudentSerializer([
        student1,
        student2,
        student3
    ],many = True)
    return Response(response.data)

# @api_view(['POST'])
# def createUserApi(request):
#     print(request.body)
#     import io 
#     stream = io.BYTESIO(request.body)
#     parsed = JSONParser().parse(stream)
#     data = serializers.StudentSerializer(data = parsed)
#     print(data.is_valid())
#     print(data.validated_data)
#     return Response({"message":"Hello"})


@api_view()
def articleApi(request):
    articles = models.Article.objects.all()
    response = serializers.ArticleSerializer(articles,many=True)
    return Response(response.data)
     
@api_view(['POST'])
def createArticleApi(request):
    body = json.loads(request.body)
    response = serializers.ArticleSerializer(body)
    return Response(response.data)