from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import delete_item, add_stock, reduce_stock
from main.views import edit_product
from main.views import add_product_ajax, get_product_json
from main.views import delete_ajax, addAmount_ajax, reduce_ajax

app_name = 'main'

urlpatterns = [
    path('',show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete-item/<int:item_id>/', delete_item, name='delete_item'),
    path('add-stock/<int:item_id>/', add_stock, name='add_stock'),
    path('reduce-stock/<int:item_id>/', reduce_stock, name='reduce_stock'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-ajax/', delete_ajax, name='delete_ajax'),
    path('addAmount-ajax/', addAmount_ajax, name='addAmount_ajax'),
    path('reduce-ajax/', reduce_ajax, name='reduce_ajax'),
]