from djangoproject.shortcuts import ReturnBuilder

rb = ReturnBuilder('djangoproject')

def index(request):
    return rb.render_to_response("index", {}, request)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print username
        print password

        return rb.HttpResponse('ok')
    else:     
        return rb.redirect('index')
