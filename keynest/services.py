
from .models import Key, Store
from .api import key_list, store_list, get_key_status


def load_keys(token):
    for item in key_list(token):
        Key.objects.update_or_create(
            keynest_id=item['KeyId'],
            defaults={
                'name': item['KeyName'],
                'property_id': item['PropertyID']
            })


def update_key_status(token, key):
    new_status = get_key_status(token, key.keynest_id)
    if new_status['ResponsePacket']:
        key.status = new_status['ResponsePacket']['Status']
        key.full_status = new_status['ResponsePacket']['FullStatus']

        key.store_name = new_status['ResponsePacket']['Store']['Name']
        key.store_address = new_status['ResponsePacket']['Store']['Address']
        key.store_time = new_status['ResponsePacket']['Store']['Storetime']
    else:
        key.status = new_status['ResponseMessage']
    key.save()


def update_keys_status(token):
    keys = Key.objects.order_by('name')[:10]
    for key in keys:
        update_key_status(token, key)


def load_stores(token):
    for item in store_list(token):
        Store.objects.update_or_create(
            store_id=item['StoreId'],
            defaults={
                'name': item['StoreName'],
                'store_time': item['StoreTime'],
                'address': item['StoreStreetAddress'],
            })

