from enum import Enum

from ..schemas import chat, document, message, user


class Model(Enum):
    User = user.User
    Chat = chat.Chat
    Message = message.Message
    Document = document.Document
