from enum import Enum

from ..models import Chat, Document, Message, User


class Model(Enum):
    User = User
    Chat = Chat
    Message = Message
    Document = Document
