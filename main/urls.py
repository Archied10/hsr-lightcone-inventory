from django.urls import path
from main.views import show_main, lightcones, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 

urlpatterns = [
    path('', show_main, name='show_main'),
    path('lightcones/', lightcones, name='lightcones'),
    path('create_item/', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]