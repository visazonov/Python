# ID_prilozheniya = 51650430
# ссылка получения токена в вк
# https://oauth.vk.com/authorize?client_id=51650430&scope=65536&response_type=token
# scope права указываем через запятую

import requests
from settings import token_vk
# импортируем print для более комфортного ввода информации
from pprint import pprint
import pandas as pd
import time

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       return response.json()


# access_token = token_vk
# user_id = '66871809'
# vk = VK(access_token, user_id)
# print(vk.users_info())


# 1
# URL = 'https://api.vk.com/method/users.get'
# params = {
#     'user_ids': '1',
#     'access_token': token_vk, # токен и версия обязательные параметры во всех запросах к VK
#     'v': '5.131'
# }
# res = requests.get(URL, params=params)
# pprint(res.json())

# 2
# URL = 'https://api.vk.com/method/users.get'
# params = {
#     'user_ids': '1,2',
#     'access_token': token_vk, # токен и версия обязательные параметры во всех запросах к VK
#     'v': '5.131',
#     'fields': 'education, sex'
# }
# res = requests.get(URL, params=params)
# pprint(res.json())

# 3
def search_groups(q, sorting=0):
    '''
    Параметры sort
    0 - сортировать по умолчанию (аналогично результ поиска в полной версии сайта);
    6 - сортировать по кол-ву пользователей
    '''
    params = {
        'q': q,
        'access_token': token_vk,  # токен и версия обязательные параметры во всех запросах к VK
        'v': '5.131',
        'sort': sorting,
        'count': 300
    }
    req = requests.get('https://api.vk.com/method/groups.search', params).json()
    # pprint(req)
    req = req['response']['items']
    return req

target_groups = search_groups('python')
# pprint(target_groups)

# из 3 получаем список для 4
target_group_uds = ','.join([str(group['id']) for group in target_groups])
# print(target_group_uds)


# 4
params = {
    'access_token': token_vk,  # токен и версия обязательные параметры во всех запросах к VK
    'v': '5.131',
    'group_ids': target_group_uds,
    'fields': 'members_count, activity, description'
}
req = requests.get('https://api.vk.com/method/groups.getById', params)

# pprint(req.json()['response'])



# Классы на примере API VK
# токен и версия могут быть разной в разных экземплярах
# базовый URL будет всегда один, в инициализации он не нужен

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def search_groups(self, q, sorting=0):
        '''
        Параметры sort
        0 - сортировать по умолчанию (аналогично результ поиска в полной версии сайта);
        6 - сортировать по кол-ву пользователей
        '''
        group_search_url = self.url + 'groups.search'
        group_search_params = {
            'q': q,
            'sort': sorting,
            'count': 300
        }
        req = requests.get(group_search_url, params={**self.params, **group_search_params}).json()
        return req['response']['items']

    def search_groups_ext(self, q, sorting=0):
        group_search_ext_url = self.url + 'groups.getById'
        target_groups = self.search_groups(q, sorting)
        target_group_uds = ','.join([str(group['id']) for group in target_groups])

        groups_info_params = {
            'group_ids': target_group_uds,
            'fields': 'members_count, activity, description'
        }
        req = requests.get(group_search_ext_url, params={**self.params, **groups_info_params}).json()
        return req['response']

    def get_followers(self, user_id=None):
        followers_url = self.url + 'users.getFollowers'
        followers_params = {
            'count': 1000,
            'user_id': user_id
        }
        res = requests.get(followers_url, params={**self.params, **followers_params}).json()
        return res['response']

    def get_groups(self, user_id=None):
        groups_url = self.url + 'groups.get'
        groups_params = {
            'count': 1000,
            'user_id': user_id,
            'extended': 1,
            'fields': 'members_count'
        }
        res = requests.get(groups_url, params={**self.params, **groups_params})
        return res.json()

    def get_news(self, query):
        groups_url = self.url + 'newsfeed.search'
        groups_params = {
            'q': query,
            'count': 200,
        }

        newsfeed_df = pd.DataFrame()  # делаем табличную структуру, включен сверху import pandas as pd

        while True:
            result = requests.get(groups_url, params={**self.params, **groups_params})
            time.sleep(0.33)

            newsfeed_df = pd.concat([newsfeed_df, pd.DataFrame(result.json()['response']['items'])])
            if 'next_from' in result.json()['response']:
                groups_params['start_from'] = result.json()['response']['next_from']
            else:
                break
        return newsfeed_df



vk_client = VkUser(token_vk, '5.131')

# получаем сообщества 'python'
# pprint(vk_client.search_groups('python'))

# по id сообществ получаем более подробную инфу о них
# pprint(vk_client.search_groups_ext('python'))

# import pandas as pd
# pd.DataFrame(vk_client.search_groups_ext('python'))
# print(pd.DataFrame(vk_client.search_groups_ext('python')))

# получаем моих подписчиков
# pprint(vk_client.get_followers())
# получаем подписчиков пользователя с ай ди 2
# pprint(vk_client.get_followers(2))

# получаем список моих сообществ
# pprint(vk_client.get_groups())
# получаем список сообществ пользователя с ID 1
# pprint(vk_client.get_groups(1))

pprint(vk_client.get_news('Короновирус'))