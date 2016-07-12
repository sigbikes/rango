from django.shortcuts import render, HttpResponse
# Import Category model for index page
from rango.models import Category, Page
from rango.forms import CategoryForm

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descinding order.
    # Retriever the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}


    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context_dict)

def about(request):

    # response = HttpResponse('Rango says "Here is an about page".')
    # response.write("<br><br><a href='/rango/'>Home</a>")

    # return response
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    # Create a context dictionary to pass to the template render engine
    context_dict = {}

    try:
        # Find a category name slug with the given name.
        # If not .get() rasies a DoesNotExist exception
        # .get() returns a model instance or throws the expcetion
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all associated Pages.
        # Note filter() returns a list of objects or an empty list
        pages = Page.objects.filter(category=category)

        # Results are added to context dictionary
        context_dict['pages'] = pages

        # Add categories as well to verify they exist
        context_dict['category'] = category
    except Category.DoesNotExist:
        # CONDITION: Category not found
        # RESULT: Do nothing and return "No Category" message
        context_dict['category'] = None
        context_dict['pages'] = None

    # Render the response back to client
    return render(request, 'rango/category.html', context_dict)

def add_category(request):

    form = CategoryForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit = True)
            # Could return a message but most recent Cats are on the index Page
            # Thus we redirect to the index
            return index(request)
        else:
            #If forms have errors - print them to the terminal.
            print(form.errors)
    # This handles bad forms, new forms, or no forms.
    # Render the for with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})
