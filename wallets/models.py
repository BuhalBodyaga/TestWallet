import uuid
from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.BigIntegerField(default=0)


class Operation(models.Model):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    OPERATION_CHOICES = [(DEPOSIT, "Deposit"), (WITHDRAW, "Withdraw")]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    operation_type = models.CharField(max_length=10, choices=OPERATION_CHOICES)
    amount = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
