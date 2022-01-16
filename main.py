from vk import VkActor
from ya import YaActor
from pprint import pprint
with open('vktoken.txt', 'r', encoding='utf-8') as f:
    vktoken = f.readline().strip('\n')
with open('yatoken.txt', 'r', encoding='utf-8') as f:
    yatoken = f.readline().strip('\n')


def backup_vk_photos():
    username = input('Введите имя пользователя')
    vkdownload = VkActor(vktoken, username, 'profile')
    yaupload = YaActor(yatoken)
    vkdownload.get_user_id()
    photos = vkdownload.get_photos()
    yaupload.make_directory(vkdownload.user_id)
    response = yaupload.upload_from_vk(photos)
    return response


pprint(backup_vk_photos())
