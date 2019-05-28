import requests


def key_list(token):
    url = 'https://api.keynest.com/api/v2/Key/KeyList'
    headers = {'ApiKey': token}
    response = requests.get(url, headers=headers)
    return response.json()['ResponsePacket']['KeyList']
