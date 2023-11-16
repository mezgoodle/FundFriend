from django.db import models

from core.abstract.models import AbstractManager, AbstractModel


class BankManager(AbstractManager):
    pass


class Bank(AbstractModel):
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)
    description = models.TextField()
    edited = models.BooleanField(default=False)

    objects = BankManager()

    def __str__(self):
        return self.author.full_name

    class Meta:
        db_table = "core.bank"
