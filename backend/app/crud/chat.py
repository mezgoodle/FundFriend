from .base import CRUD
from .enums import Model


class ChatCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.Chat.value)
