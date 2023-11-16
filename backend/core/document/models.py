from django.db import models

from core.abstract.models import AbstractManager, AbstractModel


class DocumentManager(AbstractManager):
    pass


class Document(AbstractModel):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)
    bank = models.ForeignKey(
        to="core_bank.Bank", on_delete=models.SET_NULL, null=True
    )
    edited = models.BooleanField(default=False)

    objects = DocumentManager()

    def __str__(self):
        return self.text

    class Meta:
        db_table = "core.document"
