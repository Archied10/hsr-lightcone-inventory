from django.urls import path
from main.views import show_main, lightcones, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, increase_amount, decrease_amount, delete_item, get_product_json, create_ajax, create_product_flutter, show_json_by_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('lightcones/', lightcones, name='lightcones'),
    path('create_item/', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase_amount/<int:item_id>/', increase_amount, name='increase_amount'),
    path('decrease_amount/<int:item_id>/', decrease_amount, name='decrease_amount'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('json-user/', show_json_by_user, name='show_json_by_user'),
]