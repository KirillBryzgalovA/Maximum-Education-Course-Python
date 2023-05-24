import vk_api
from course import *
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course
from wiki import get_wiki_article

my_token = 'vk1.a.zx9qvSsJXa10pcWXEAgnf_joYO6noueBNEwRKy2iSwlLgg6DrjlunfMp3Z2a_UYVSdUWAbAODdWu3daZKoet8UoS-Q9KwJ40na5UxvyTOpP26d3ZJTGJac-XcKUM-7Zg2syQxThIluYWNEBX23LOjatyQbD_ybsEysNj91RcimTbjWxVz0a9roZMJU9pzFteIc36K0ZkfJwE7JBJ8wxzvA'

vk_session = vk_api.VkApi(token=my_token)
vk_session._auth_token()
longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        message_id = event.message_id
        message_text = event.text.lower()
        
        print(user_id, message_id, message_text)

        if message_text == "-к":
            response = f'{get_course("R01235")} рублей за 1 доллар' \
                    f'{get_course("R01375")} рублей за 1 юань\n {get_course("R01035")} рублей за 1 фунт'
        elif message_text == "-к доллар":
            response = f'{get_course("R01235")} рублей за 1 доллар'
        elif message_text == "-к евро":
            response = f'{get_course("R01239")} рублей за 1 евро'
        elif message_text == "-к фунт":
            response = f'{get_course("R01035")} рублей за 1 фунт'
        elif message_text == "-к юань":
            response = f'{get_course("R01375")} рублей за 1 юань'
        elif message_text.startswith('-в'):
            article = message_text[2:]
            response = get_wiki_article(article)
            if len(response) >= 4000:
                response = response[0:4000]
        else:
            response = "Извини, такой команды к сожалению не существует :("
            
        vk.messages.send(user_id=user_id, random_id=message_id, message=response)
