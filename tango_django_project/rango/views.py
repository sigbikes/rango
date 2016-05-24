from django.shortcuts import render, HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{boldmessage}} in the template!
    context_dict = {'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)



def about(request):
    response = HttpResponse('Rango says "Here is an about page".')
    response.write("<br><br><a href='/rango/'>Home</a>")

    return response
