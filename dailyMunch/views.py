from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from registration.signals import user_registered
from dailyMunch.forms import *
from dailyMunch.models import *
from yelp import Yelp

# Create your views here.
def index(request):
    context = {}
    if request.method != 'POST':
        context['form'] = NewSearchForm()
    else:
        form = NewSearchForm(request.POST)
        print(request.POST)
        if "submit" in request.POST.get("action") and form.is_valid():
            # print("********************************************", form.cleaned_data)
            attrs = []
            if form.cleaned_data.get('trendy'):
                attrs.append('hot_and_new')
            if form.cleaned_data.get('reservation'):
                attrs.append('reservation')
            yelp_params = {
                'term': form.cleaned_data.get('search_term'),
                'location': form.cleaned_data.get('location'),
                'radius': form.cleaned_data.get('distance') * 1609,
                'price': ', '.join([str(i) for i in range(1, int(form.cleaned_data.get('price')))]),
                'open_now': form.cleaned_data.get('open_now'),
                'attributes': ', '.join(attrs)
            }
            request.session['form'] = {
                'keyword': form.cleaned_data.get('search_term'),
                'location': form.cleaned_data.get('location'),
                'distance_miles': form.cleaned_data.get('distance'),
                'price': form.cleaned_data.get('price'),
                'open_now': form.cleaned_data.get('open_now'),
                'trendy': form.cleaned_data.get('trendy'),
                'reservation': form.cleaned_data.get('reservation'),
                'pickup' : form.cleaned_data.get('pickup'),
                'delivery': form.cleaned_data.get('delivery'),
            }
            # print(yelp_params)
            results = Yelp.businessSearch(yelp_params)
            # print(results)
            if 'businesses' in results:
                for result in results['businesses'].copy():
                    if (form.cleaned_data.get('pickup') and 'pickup' not in result['transactions']) or (form.cleaned_data.get('delivery') and 'delivery' not in result['transactions']): #result['id'] in resto_list or
                        results['businesses'].remove(result)
            # context['results'] = results['businesses']
            request.session["results"] = results['businesses']
            request.session["result"] = request.session["results"].pop(0)
            context["result"] = request.session["result"]
            request.session.modified = True
        elif "no" in request.POST.get("action"):
            if request.session["results"]:
                request.session["result"] = request.session["results"].pop(0)
                context["result"] = request.session["result"]                
                request.session.modified = True
            else:
                context["result"] = False
        elif "yes" in request.POST.get("action"):
            return redirect(reverse('addrestaurant'))
                #Needs to redirect ot page where user can either log in or create an account dong so without losing the restaurant they clicked yes on
        # print(request.session["results"])
        context['form'] = form
    return render(request, 'dailyMunch/index.html', context)



def about(request):
    return render(request, 'dailyMunch/about.html')

@login_required
def dashboard(request):
    return render(request, 'dailyMunch/dashboard.html')

@login_required
def addrestaurant(request):
    print(request.session['result'])
    current_yelp_id = request.session['result']['id']
    restaurant, created = Restaurant.objects.get_or_create(yelp_id=current_yelp_id, defaults={'data': request.session['result']})
    visited = Visited(user=request.user, restaurant=restaurant)
    visited.save()
    #user data is updated and ready to be pre-loaded for next query
    Profile.objects.filter(user=request.user).update(**request.session['form'])
    return redirect(reverse('dashboard'))
    # TODO: Load the profile inot the form if the user is logged in
    # TODO: Create fucntionality for choosing a resturant from restaurants that have already been visited
    # TODO: If they want to choose a new restuartans and they are logged in then we need to filter out restuarants that they've visted
    # TODO: Display last few restaurants on Dahsboard
    # TODO: Having link that user can click on to take them to new query

@receiver(user_registered)
def new_user(sender, user, request, **kwargs):
    form = request.session.get('form')
    if form is not None:
        profile = Profile.objects.create(user=user, **form)
        current_yelp_id = request.session['result']['id']
        restaurant, created = Restaurant.objects.get_or_create(yelp_id=current_yelp_id, defaults={'data': request.session['result']})
        visited = Visited.objects.create(user=user, restaurant=restaurant)
    else:
        profile = Profile.objects.create(user=user)


