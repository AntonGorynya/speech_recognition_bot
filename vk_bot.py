from environs import Env
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


if __name__ == '__main__':
    env = Env()
    env.read_env()
    bot_token = env('VK_TOKEN')
    google_key = env('GOOGLE_KEY')
    project_id = env('PROJECT_ID')

    vk_session = vk_api.VkApi(token=bot_token)

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            if event.to_me:
                print('Для меня от: ', event.user_id)
            else:
                print('От меня для: ', event.user_id)
            print('Текст:', event.text)