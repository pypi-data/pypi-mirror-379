from typing import Any

from bs4 import BeautifulSoup
from requests import get, post

_BASE_URL = 'https://mail.remotix.app'

class Message:
    def __init__(self, data: dict[str, Any]):
        self.id = data['id']
        self.receiver = data['to_address']
        self.sender = data['from_address']
        self.subject = data['subject']
        self.body = data['body']
        self.html = BeautifulSoup(data['html_body'], 'html.parser')
        self.received_at = data['received_at']

    def __str__(self):
        return self.body.replace('\r\n', ' ').replace('\n', ' ')[:100] + ('...' if len(self.body) > 100 else '')

    def __repr__(self):
        return f'<Message id={self.id} sender={self.sender} subject={self.subject}>'

def messages(email: str) -> list[Message]:
    return [Message(message) for message in get(f'{_BASE_URL}/api/messages/{email}/').json()]

def domains() -> list[str]:
    return [domain.get('name') for domain in get(f'{_BASE_URL}/api/domains').json()]

def email(address: str) -> bool:
    return post(f'{_BASE_URL}/api/addresses/', json={"address": address}).status_code == 201


if __name__ == '__main__':
    print(email('julie678814@asdfar.xyz'))
