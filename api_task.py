# задача 1
import requests

sh = ['Hulk', 'Captain America', 'Thanos']

base_host = 'https://akabab.github.io/superhero-api/api'
def get_headers():
    return {
        'Content-Type': 'application/json',
    }
def get_intelligence_sh(sh_list):
    uri = '/all.json'
    request_url = base_host + uri
    response = requests.get(request_url)
    print(response.status_code)
    # print(response.json())
    hero = []
    intelligence = []
    for info_hero in response.json():
        # print(info_hero)
        # print()
        if info_hero['name'] in sh_list:
            # print('Ура')
            hero.append(info_hero['name'])
            intelligence.append(info_hero['powerstats']['intelligence'])

    print(hero)
    print(intelligence)

    res = sorted(list(zip(hero, intelligence)))
    print(f'Самый умный {res[-1][0]}')


# get_intelligence_sh(sh)




# задача 2
import requests
class YaUploader:
    base_host = 'https://cloud-api.yandex.net'
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = '/v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def upload(self, file_path: str):
        yandex_path = '/new/' + name
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(file_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка прошла успешно')


if __name__ == '__main__':
    from settings import TOKEN

    # path_to_file = input('Введите адрес')
    # path_to_file = 'file1.txt'
    path_to_file = 'C:/Users/User/Desktop/Hello.txt'

    name = path_to_file.strip().split("/")[-1]

    uploader = YaUploader(TOKEN)
    # result = uploader.upload(path_to_file)