from django.shortcuts import render
from django.views.generic.list import ListView
from fire.models import Locations, Incident, FireStation


class HomePageView(ListView):
    model = Locations
    context_object_name = 'home'
    template_name = "home.html"



def map_station(request):
    # Fetch fire station data: name, latitude, and longitude
    fireStations = FireStation.objects.values('name', 'latitude', 'longitude')
    
    # Convert latitude and longitude to float for consistent numerical representation
    for fs in fireStations:
        fs['latitude'] = float(fs['latitude'])
        fs['longitude'] = float(fs['longitude'])
    
    # Convert QuerySet to a list for easier manipulation and template usage
    fireStations_list = list(fireStations)
    
    # Pass the data to the context for rendering in the template
    context = {
        'fireStations': fireStations_list,
    }
    
    # Render the map_station.html template with the provided context
    return render(request, 'map_station.html', context)
