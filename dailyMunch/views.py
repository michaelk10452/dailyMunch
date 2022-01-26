from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from registration.signals import user_registered
from dailyMunch.forms import *
from dailyMunch.models import *
from yelp import Yelp

# Create your views here.
def index(request):
    context = {}
    if request.method != 'POST':
        if request.user.is_authenticated and Profile.objects.get(user=request.user).keyword != '':
            profile = model_to_dict(Profile.objects.get(user=request.user))
            print(profile)
            profile.pop('user')

            context['form'] = NewSearchForm(profile)
        else:
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
                'term': form.cleaned_data.get('keyword'),
                'location': form.cleaned_data.get('location'),
                'radius': form.cleaned_data.get('distance_miles') * 1609,
                'price': ', '.join([str(i) for i in range(1, int(form.cleaned_data.get('price')))]),
                'open_now': form.cleaned_data.get('open_now'),
                'attributes': ', '.join(attrs)
            }
            request.session['form'] = form.cleaned_data
            # {
            #     'keyword': form.cleaned_data.get('keyword'),
            #     'location': form.cleaned_data.get('location'),
            #     'distance_miles': form.cleaned_data.get('distance_miles'),
            #     'price': form.cleaned_data.get('price'),
            #     'open_now': form.cleaned_data.get('open_now'),
            #     'trendy': form.cleaned_data.get('trendy'),
            #     'reservation': form.cleaned_data.get('reservation'),
            #     'pickup' : form.cleaned_data.get('pickup'),
            #     'delivery': form.cleaned_data.get('delivery'),
            # }
            # print(yelp_params)
            results = Yelp.businessSearch(yelp_params)
            # print(results)
            if 'businesses' in results:
                for result in results['businesses'].copy():
                    if (form.cleaned_data.get('pickup') and 'pickup' not in result['transactions']) or (form.cleaned_data.get('delivery') and 'delivery' not in result['transactions']): #result['id'] in resto_list or
                        results['businesses'].remove(result)
            # context['results'] = results['businesses']
            request.session["results"] = results['businesses']
            result = request.session["results"].pop(0)
            if request.user.is_authenticated:
                visiteds = Visited.objects.filter(user=request.user)
                yelp_ids = {v.restaurant.yelp_id for v in visiteds}
                while result['id'] in yelp_ids:
                    result = request.session["results"].pop(0)
            request.session["result"] = result
            context["result"] = result
            request.session.modified = True
        elif "no" in request.POST.get("action"):
            if request.session["results"]:
                result = request.session["results"].pop(0)
                if request.user.is_authenticated:
                    visiteds = Visited.objects.filter(user=request.user)
                    yelp_ids = {v.restaurant.yelp_id for v in visiteds}
                    while result['id'] in yelp_ids:
                        result = request.session["results"].pop(0)
                request.session["result"] = result
                context["result"] = result              
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
    context = {}
    visiteds = Visited.objects.filter(user=request.user)
    categories = {c['title'] for v in visiteds for c in v.restaurant.data['categories']}
    rest_objs = Restaurant.objects.filter(id__in=visiteds.values_list("restaurant", flat=True))
    rest_cats = {r.yelp_id: [c['title'] for c in r.data['categories']] for r in rest_objs }
    rest_visits = {r.yelp_id: visiteds.filter(restaurant=r).count() for r in rest_objs }
    categories = {c: {"restaurants": len([r for r, cats in rest_cats.items() if c in cats]), "visits": sum([rest_visits[r] for r, cats in rest_cats.items() if c in cats])} for c in categories}
    print(categories)
    if "category" in request.GET:
        category = request.GET['category']
        yelp_ids = {v.restaurant.yelp_id for v in visiteds for c in v.restaurant.data['categories'] if c['title'] == category}
        context["category_restaurants"] = [r.data for r in Restaurant.objects.filter(yelp_id__in=yelp_ids)]
    context["categories"] = categories
    return render(request, 'dailyMunch/dashboard.html', context)

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
    # TODO: When displaying old restaurants sort by number of times they've been visited
    # TODO: Put data in a table
    # TODO: Sort by visits
    # TODO: Host the site
    # TODO: Make Footer and Tags better

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


