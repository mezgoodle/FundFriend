from .base import CRUD
from .enums import Model


class MessageCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.Message.value)
