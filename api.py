import requests
from settings import TOKEN
class Yandex:
    base_host = 'https://cloud-api.yandex.net'
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        uri = '/v1/disk/resources/files/'
        request_url = self.base_host + uri
        params = {'limit': 2}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.status_code)
        print(response.json())

    def _get_upload_link(self, path):
        uri = '/v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def upload_to_disk(self, lokal_path, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(lokal_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка прошла успешно')

    def upload_from_internet(self, url, yandex_path):
        uri = '/v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'url': url, 'path': yandex_path}
        responce = requests.post(request_url, params=params, headers=self.get_headers())
        print(responce.json())



if __name__ == '__main__':
    ya = Yandex(TOKEN)

    # ya.get_files_list()

    import os
    # ya.upload_to_disk('folder/1.txt', '/new/world.txt')
    # ya.upload_to_disk('C:/Users/User/Desktop/Python/folder/1.txt', '/new/world1.txt')
    # image_url = 'https://mobimg.b-cdn.net/v3/fetch/a2/a2d0571178a1a205aac1139e100ed1a8.jpeg'
    # ya.upload_from_internet(image_url, '/mountains3.jpg')



class Reddit:
    def get_top_gifs(self):
        url = 'https://reddit.com/r/gifs/top.json?t=day'
        headers = {"User-Agent": 'netology'}
        response = requests.get(url, headers=headers)
        data = response.json()
        print(len(data['data']))

if __name__ == '__main__':
    reddit = Reddit()
    reddit.get_top_gifs()