import requests
import json


def get_id_token(url, headers, payload):
    url = url + 'chat/spare?crm=TEST&domain=test'
    response = requests.get(url, headers=headers, data=payload)
    id = response.id
    token = response.token
    return id, token


def get_status(url, headers, id, token):
    method = 'status'
    url = url + f'instance{id}/{method}?token={token}'
    response = requests.get(url, headers=headers)
    return response.state


def get_name_and_number(url, headers, id, token):
    method = 'contacts'
    url = url + f'instance{id}/{method}?token={token}'
    response = requests.get(url, headers=headers)
    number = response.number
    name = response.name
    return number, name


def send_message(url, headers, id, token, number):
    method = 'sendMessage'
    url = url + f'instance{id}/{method}?token={token}'
    payload = {'phone': number,
               'body': 'текст сообщения',
               'sendSeen': '1',
               'typeMsg': 'text',
               }
    response = requests.post(url, data=payload, headers=headers)
    return response.status_code


def main():
    url = "https://dev.whatsapp.sipteco.ru/v3/"

    payload = {}
    headers = {
        'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'
    }
    id, token = get_id_token(url, headers=headers, payload=payload)
    status = get_status(url=url, headers=headers, id=id, token=token)
    name, number = get_name_and_number(
        url=url,
        headers=headers,
        id=id, token=token)
    send_message(url=url, headers=headers, id=id, token=token, number=number)
    data_set = {
        'name': name,
        'phone': number,
        'status': status,
        'id': id,
        'token': token
        }
    json.dumps(data_set)


if __name__ == '__main__':
    main()
