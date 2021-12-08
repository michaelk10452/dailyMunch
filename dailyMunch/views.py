from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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
                context["result"] = request.session["results"].pop(0)
                request.session.modified = True
            else:
                context["result"] = False
        elif "yes" in request.POST.get("action"):
            if request.user.get_username():
                print('user is logged in')

            else:
                return redirect(reverse('addrestaurant'))
                #Needs to redirect ot page where user can either log in or create an account dong so without losing the restaurant they clicked yes on
        # print(request.session["results"])
        context['form'] = form
    return render(request, 'dailyMunch/index.html', context)



def about(request):
    return render(request, 'dailyMunch/about.html')



@login_required
def addrestaurant(request):
    pass
    # extract yelp id from your request.session['result]
    # check if yelp id exists in restaurant table
        # Restaurant.objects.filter(yelp_id=current_yelp_id)
    # check if above query has any results, if empty set then add the new restaurant to the Restaurant table
    # check if restaurant has not been visited by User then link that Restaurant to the currrent User
