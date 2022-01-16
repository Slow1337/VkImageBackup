import requests


class YaActor():
    def __init__(self, token: str):
        self.token = token
        self.uri = 'https://cloud-api.yandex.net/v1/disk/'
        self.path = ''

    def make_directory(self, path: str):
        """Метод создает папку на яндекс.диске"""
        self.path = path
        method = 'resources'
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        params = {
            'path': path
        }
        url = f'{self.uri}{method}'
        response = requests.put(url=url, headers=headers, params=params)
        return response

    def upload_from_vk(self, some_dict: dict):
        """Метод принимает словарь и загружает фото на я.диск, ключ выступает
        названием файла, а ссылка должна быть значением"""
        method = 'resources/upload'
        url = f'{self.uri}{method}'
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        overall_response = []
        for name in some_dict:
            path = f'{self.path}/{name}.jpg'
            photo_link = some_dict[name]
            params = {
                'path': path,
                'url': photo_link
            }
            response = requests.post(url=url, headers=headers, params=params)
            response = response.json()
            final = requests.get(url=response['href'], headers=headers)
            final = final.json()
            overall_response.append(final)
        return overall_response
        #     overall_response.append(response)
        # return overall_response
