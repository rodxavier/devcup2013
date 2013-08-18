from djangoproject.shortcuts import ReturnBuilder
from django.contrib.auth import authenticate
from accounts.models import User

rb = ReturnBuilder('djangoproject')

def index(request):
    return rb.render_to_response("index", {}, request)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        email = request.POST['email']
        mobile = request.POST['mobile']

        try:
            user = User.objects.create_user(username=username, 
                                            email=email, 
                                            password=password, 
                                            mobile=mobile)

            if user is not None:
                authenticate(username=username, password=password)
                return rb.HttpResponse('true')
            else:
                return rb.HttpResponse('Registration Failed!')

        except Exception, e:
            return rb.HttpResponse(e.message.capitalize())

    else:     
        return rb.redirect('index')

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
