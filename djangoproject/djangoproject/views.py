from djangoproject.shortcuts import ReturnBuilder
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from accounts.models import User
from djangoproject.forms import CreateDealForm, CreateOfferForm
from marketplace.models import Deal, Offer
from django.shortcuts import redirect

rb = ReturnBuilder('djangoproject')

def index(request):
    return rb.render_to_response("index", {}, request)

def accept_offer(request, id):
    offer = Offer.objects.get(pk=id)
    deal_id = offer.deal_offered_to.id

    offer.accept_offer()

    return redirect("/deal/" + str(deal_id))

def reject_offer(request, id):
    user = request.user

    offer = Offer.objects.get(pk=id)
    deal_id = offer.deal_offered_to.id

    offer.is_rejected = True
    offer.save()

    return redirect("/deal/" + str(deal_id))

def deal(request, id):

    if request.method == 'POST':
        form = CreateOfferForm(request.POST)

        if form.is_valid():
            form.save()



    d = Deal.objects.get(pk=id)

    user_available_deals = Deal.objects.filter(owner=request.user, is_available=True)

    data = {
        'deal': d,
        'yours': d.owner == request.user,
        'offers': d.deal_offered_to.all(),
        'user_available_deals': user_available_deals
    }

    return rb.render_to_response("deal_page", data, request)

def account(request, id):
    user = User.objects.get(pk=id)

    deals = Deal.objects.filter(owner=user).order_by('-created_at')

    data = {
        'deals': deals,
        'other_user': user
    }
    return rb.render_to_response("account", data, request)


def search(request, query):
    deals = Deal.objects.search(query).order_by('-created_at')

    data = {
        'deals': deals,
        'search_query': query
    }
    return rb.render_to_response("search_results", data, request)

def create_deal(request):
    if request.method == 'POST':
        create_form = CreateDealForm(request.POST, request.FILES)

        if create_form.is_valid():
            deal = create_form.save(commit=False)
            deal.owner = request.user
            deal.save()

            return rb.render_to_response('create_deal', {}, request)            

        else:
            return rb.render_to_response('create_deal', {}, request)
            
    else:
        return rb.render_to_response('create_deal', {}, request)

@login_required(login_url='/')
def dashboard(request):
    user = request.user

    deals = Deal.objects.filter(owner=user).order_by('-created_at')
    offers = Offer.objects.filter(owner=user).order_by('-created_at')

    data = {
        'deals': deals,
        'offers': offers
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
