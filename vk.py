import requests
from time import ctime


class VkActor():
    def __init__(self, token: str, user_id: str, album_id, amount=5):
        self.token = token
        self.album_id = album_id
        self.amount = amount
        self.uri = 'https://api.vk.com/method/'
        self.user_id = user_id

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
