from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties


@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    """
    View to return all properties with Redis caching for 15 minutes
    """
    properties = get_all_properties()
    
    # Convert to list of dictionaries for JSON response
    property_data = []
    for property in properties:
        property_data.append({
            'id': property.id,
            'title': property.title,
            'description': property.description,
            'price': str(property.price),
            'location': property.location,
            'created_at': property.created_at.isoformat(),
        })
    
    return JsonResponse({
        'properties': property_data,
        'count': len(property_data)
    })
