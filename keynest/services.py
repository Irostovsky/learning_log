
from .models import Key
from .api import key_list#, stores


def load_keys(token):
    for item in key_list(token):
        Key.objects.update_or_create(
            keynest_id=item['KeyId'],
            defaults={
                'name': item['KeyName']
            })

def load_stores(token):
    pass
    # for item in stores(token):
    #     if not Key.objects.filter(keynest_id=item['KeyId']):
    #         key = Key(keynest_id=item['KeyId'], name=item['KeyName'])
    #         key.save()

