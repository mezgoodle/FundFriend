from .base import CRUD
from .enums import Model


class DocumentCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.Document.value)
