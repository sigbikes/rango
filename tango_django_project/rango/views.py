from django.shortcuts import render, HttpResponse
# Import Category model for index page
from rango.models import Category

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descinding order.
    # Retriever the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}


    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context_dict)

def about(request):

    # response = HttpResponse('Rango says "Here is an about page".')
    # response.write("<br><br><a href='/rango/'>Home</a>")

    # return response
    return render(request, 'rango/about.html')
