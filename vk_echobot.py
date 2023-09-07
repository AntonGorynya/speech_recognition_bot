import random
from environs import Env

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from dialog_flow_common import  detect_intent_text


def echo(event, vk_api, project_id):
    response = detect_intent_text(project_id, event.user_id, event.text)
    if not response.query_result.intent.is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=response.query_result.fulfillment_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    env = Env()
    env.read_env()
    bot_token = env('VK_TOKEN')
    google_key = env('GOOGLE_KEY')
    project_id = env('PROJECT_ID')

    vk_session = vk.VkApi(token=bot_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api, project_id)
