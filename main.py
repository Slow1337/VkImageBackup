from vk import VkActor
from ya import YaActor
import logging
with open('vktoken.txt', 'r', encoding='utf-8') as f:
    vktoken = f.readline().strip('\n')
with open('yatoken.txt', 'r', encoding='utf-8') as f:
    yatoken = f.readline().strip('\n')
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('main_logger')


def backup_vk_photos():
    log.info('Программа начинает свою работу')
    userid = input('Введите id пользователя: ')
    log.info('Пользователем задан user_id для VkActor')
    vkdownload = VkActor(vktoken, userid, 'profile')
    log.info('Создана инстанция класса VkActor')
    yaupload = YaActor(yatoken)
    log.info('Создана инстанция класса YaActor')
    photos = vkdownload.get_photos()
    log.info('Получен список фотографий пользователя в его профиле')
    yaupload.make_directory(vkdownload.user_id)
    log.info('Создана папка на я.диске')
    yaupload.upload_from_vk(photos)
    log.info('Фото отправлены на загрузку')


backup_vk_photos()
