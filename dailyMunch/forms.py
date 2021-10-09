from django import forms



class NewSearchForm(forms.Form):
    search_term = forms.CharField(max_length=200, label='What food, cuisine, drink, etc. are you thinking about?')
    location = forms.CharField(max_length=200, label='What city?')
    distance = forms.IntegerField(min_value=4, max_value=24)
    #look up code to build a slider for distance
    PRICE_CHOICES=[('1','$'),
             ('2','$$'),
             ('3', '$$$'),
             ('4', '$$$$')]
    price = forms.ChoiceField(choices=PRICE_CHOICES, widget=forms.RadioSelect)
    open_now = forms.BooleanField(initial=True, required=False)
    trendy = forms.BooleanField(initial=False, required=False)
    reservation = forms.BooleanField(initial=False, required=False)
    pickup = forms.BooleanField(initial=False, required=False)
    delivery = forms.BooleanField(initial=False, required=False)


