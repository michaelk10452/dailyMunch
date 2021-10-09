from django.shortcuts import render
from dailyMunch.forms import *
from yelp import Yelp

# Create your views here.

def index(request):
    context = {}
    if request.method != 'POST':
        context['form'] = NewSearchForm()
    else:
        form = NewSearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
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
            print(yelp_params)
            results = Yelp.businessSearch(yelp_params)
            print(results)
            if 'businesses' in results:
                for result in results['businesses'].copy():
                    if (form.cleaned_data.get('pickup') and 'pickup' not in result['transactions']) or (form.cleaned_data.get('delivery') and 'delivery' not in result['transactions']): #result['id'] in resto_list or
                        results['businesses'].remove(result)
            context['results'] = results['businesses']
        context['form'] = form
    return render(request, 'dailyMunch/index.html', context)