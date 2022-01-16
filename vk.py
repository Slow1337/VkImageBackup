import requests
from time import ctime


class VkActor():
    def __init__(self, token: str, username: str, album_id, amount=5):
        self.token = token
        self.username = username
        self.album_id = album_id
        self.amount = amount
        self.uri = 'https://api.vk.com/method/'
        self.user_id = ''

    def get_user_id(self):
        """Получить id по короткому имени и записать его в аттрибут объекта"""
        method = 'utils.resolveScreenName'
        params = {
            'screen_name': self.username,
            'access_token': self.token,
            'v': '5.131'
        }
        response = requests.get(url=f'{self.uri}{method}', params=params)
        response = response.json()
        self.user_id = str(response['response']['object_id'])
        # return response
        # пока возврат вроде не нужен, но может быть нужен потом
        # для загрузки фото из сообществ вк, там id должно идти с - в начале

    def get_photos(self):
        """Получает ссылки на фотографии, по аттрибуту user_id,после чего
        возвращает словарь, где количество лайков(или лайки+дата) - ключ,
        а ссылка на фото - значение"""
        method = 'photos.get'
        params = {
            'access_token': self.token,
            'owner_id': self.user_id,
            'album_id': self.album_id,
            'count': self.amount,
            'photo_sizes': 1,
            'extended': 1,
            'v': '5.131'
        }
        response = requests.get(url=f'{self.uri}{method}', params=params)
        response = response.json()
        file_link_dict = {}
        items = response['response']['items']
        for item in items:
            value = item['sizes'][-1]['url']
            key = item['likes']['count']
            date = ctime(item['date'])
            if key in file_link_dict:
                file_link_dict.update({f'{key}{date}': value})
            else:
                file_link_dict.update({f'{key}': value})
        return file_link_dict

        # тут надо, чтобы возвращался словарь лайки: ссылка
        # дубли должны иметь вид лайк + дата загрузки: ссылка
