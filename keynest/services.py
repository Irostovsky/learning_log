
from .models import Key
from .api import key_list


def load_keys(token):
    for item in key_list(token):
        if not Key.objects.filter(keynest_id=item['KeyId']):
            key = Key(keynest_id=item['KeyId'], name=item['KeyName'])
            key.save()

