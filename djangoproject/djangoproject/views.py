from djangoproject.shortcuts import ReturnBuilder
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from accounts.models import User

rb = ReturnBuilder('djangoproject')

def index(request):
    return rb.render_to_response("index", {}, request)

@login_required(login_url='/')
def dashboard(request):
    user = request.user

    print user.email

    data = {

    }
    return rb.render_to_response("dashboard", data, request)

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
                authenticated_user= authenticate(username=username, password=password)
                authenticated_user.backend = "django.contrib.auth.backends.ModelBackend"
                django_login(request, authenticated_user)

                return rb.HttpResponse('true')
            else:
                return rb.HttpResponse('Registration Failed!')

        except Exception, e:
            return rb.HttpResponse(e.message.capitalize())

    else:     
        return rb.redirect('index')

def logout(request):
    django_logout(request)

    return rb.redirect('index')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            user.backend = "django.contrib.auth.backends.ModelBackend"
            django_login(request, user)

            return rb.HttpResponse('true')
        else:
            return rb.HttpResponse('false')
    else:     
        return rb.redirect('index')
