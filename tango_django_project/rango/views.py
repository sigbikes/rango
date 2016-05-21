from django.shortcuts import render, HttpResponse

def index(request):
    response = HttpResponse("Rango says hey there partner!")
    response.write("<br>")
    response.write("<a href='/rango/about'>About</a>")
    return response



def about(request):
    response = HttpResponse('Rango says "Here is an about page".')
    response.write("<br><br><a href='/rango/'>Home</a>")

    return response
