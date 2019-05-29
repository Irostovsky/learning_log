
from .models import Key, Store
from .api import key_list, store_list


def load_keys(token):
    for item in key_list(token):
        Key.objects.update_or_create(
            keynest_id=item['KeyId'],
            defaults={
                'name': item['KeyName'],
                'property_id': item['PropertyID']
            })


def load_stores(token):
    for item in store_list(token):
        Store.objects.update_or_create(
            store_id=item['StoreId'],
            defaults={
                'name': item['StoreName'],
                'store_time': item['StoreTime'],
                'address': item['StoreStreetAddress'],
            })

