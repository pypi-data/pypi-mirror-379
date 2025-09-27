import os
from dotenv import load_dotenv


load_dotenv()


URL_API = os.environ.get('URL_API')
TOKEN_API = os.environ.get('TOKEN_API')
TEST_CONTACT_ID = os.environ.get('TEST_CONTACT_ID')

END_CHATS_WITH_ATTENDANTS_LAST_MESSAGE = bool(os.environ.get('END_CHATS_WITH_ATTENDANTS_LAST_MESSAGE') == 'True')
END_CHATS_WITH_CONTACTS_LAST_MESSAGE = bool(os.environ.get('END_CHATS_WITH_CONTACTS_LAST_MESSAGE') == 'True')
TIMEOUT = int(os.environ.get('TIMEOUT'))
ALERT_TIME = float(os.environ.get('ALERT_TIME'))
ALERT_MESSAGE_TEXT = '''
🔔 Olá! Percebemos que você está inativo há algum tempo.
Para otimizar nosso atendimento, esta conversa será encerrada.
Caso precise de algo, é só nos chamar novamente.

👋 Agradecemos o contato e estamos à disposição!
'''