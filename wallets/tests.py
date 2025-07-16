import pytest
from rest_framework.test import APIClient
from .models import Wallet


@pytest.mark.django_db
def test_deposit_and_withdraw():
    client = APIClient()
    wallet = Wallet.objects.create(balance=1000)

    response = client.post(
        f"/api/v1/wallets/{wallet.id}/operation",
        {"operation_type": "DEPOSIT", "amount": 500},
        format="json",
    )
    assert response.status_code == 200
    assert response.data["balance"] == 1500

    response = client.post(
        f"/api/v1/wallets/{wallet.id}/operation",
        {"operation_type": "WITHDRAW", "amount": 200},
        format="json",
    )
    assert response.status_code == 200
    assert response.data["balance"] == 1300
