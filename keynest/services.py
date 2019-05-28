
import requests
from .models import Key


def load_keys():
    token = 'a5488c6ddc1c495e88e6477f9ee864a2'
    url = 'https://api.keynest.com/api/v2/Key/KeyList'
    headers = {'ApiKey': token}
    response = requests.get(url, headers=headers)
    all_keys = response.json()['ResponsePacket']['KeyList']
    for item in all_keys:
        if not Key.objects.filter(keynest_id=item['KeyId']):
            key = Key(keynest_id=item['KeyId'],
                       name=item['KeyName'])
            key.save()

