from django.shortcuts import render
from django.http import HttpResponse


def projects(request)-> str:
    return HttpResponse("Here are our products")

def project(request, pk) -> str:
    return HttpResponse("Single project with key is " + str(pk))