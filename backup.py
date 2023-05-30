# user_id = str(input('Введите id пользователя'))
user_id = '66871809'
# input('Введите токен')

import requests
from pprint import pprint
from settings import TOKEN
from settings import token_vk

class Yandex:
    base_host = 'https://cloud-api.yandex.net'
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, path):
        uri = '/v1/disk/resources/'
        create_url = self.base_host + uri
        params = {'path': path}
        response = requests.put(create_url, headers=self.get_headers(), params=params)
        with open('folder/logs_backup.txt', 'at', encoding='utf-8') as new_file:
            new_file.write(f'создание папки {path}: {response.status_code} {response.json()}\n')

    def upload_from_internet(self, url, yandex_path):
        uri = '/v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'url': url, 'path': yandex_path}
        response = requests.post(request_url, params=params, headers=self.get_headers())
        with open('folder/logs_backup.txt', 'at', encoding='utf-8') as new_file:
            new_file.write(f'загрузка: код {response.status_code} {response.json()}\n')

if __name__ == '__main__':
    ya = Yandex(TOKEN)

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def _get_photos(self, id):
        get_photos_url = self.url + 'photos.get'
        get_photos_params = {
            'owner_id': id,
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1
        }
        req = requests.get(get_photos_url, params={**self.params, **get_photos_params}).json()
        return req

    def upload_photos(self, id):
        req = self._get_photos(id)
        info_list = []
        for request in req['response']['items'][0:5:]:
          info_file = {
              "file_name": str(request['likes']['count']) + '.jpg',
              "size": request['sizes'][-1]['type']
          }
          url = request['sizes'][-1]['url']
          file_name = str(request['likes']['count']) + '.jpg'
          path_name = '/backup/' + file_name
          info_list.append(info_file)

          ya.upload_from_internet(url, path_name)

        with open('folder/file2.txt', 'at', encoding='utf-8') as new_file:
            new_file.write(f'загружены файлы: {info_list}\n')

vk_client = VkUser(token_vk, '5.131')

# создание папки
ya.create_folder('/backup/')  # логи записывает
# ya.create_folder('/new/backup/')

# Загрузка фотографии
vk_client.upload_photos(user_id)

