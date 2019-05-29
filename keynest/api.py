import requests


def key_list(token):
    url = 'https://api.keynest.com/api/v2/Key/KeyList'
    headers = {'ApiKey': token}
    response = requests.get(url, headers=headers)
    return response.json()['ResponsePacket']['KeyList']


def store_list(token):
    url = 'https://api.keynest.com/api/v2/KeyStore/List'
    headers = {'ApiKey': token}
    response = requests.get(url, headers=headers)
    return response.json()['ResponsePacket']['StoreList']


def get_key_status(token, key_id):
    url = 'https://api.keynest.com/api/v2/Key/GetKeyStatus'
    headers = {'ApiKey': token}
    params = {'KeyId': key_id}
    response = requests.post(url, data=params, headers=headers)
    return response.json()
