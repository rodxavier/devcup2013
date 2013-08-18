from djangoproject.shortcuts import ReturnBuilder
from django.contrib.auth import authenticate

rb = ReturnBuilder('djangoproject')

def index(request):
    return rb.render_to_response("index", {}, request)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            return rb.HttpResponse('true')
        else:
            return rb.HttpResponse('false')
    else:     
        return rb.redirect('index')
