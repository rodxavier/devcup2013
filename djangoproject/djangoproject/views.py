from djangoproject.shortcuts import ReturnBuilder

rb = ReturnBuilder('djangoproject')

def index(request):
    return rb.render_to_response("index", {}, request)

