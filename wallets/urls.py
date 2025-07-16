from django.urls import path
from .views import WalletOperationView, WalletBalanceView

urlpatterns = [
    path('<uuid:wallet_id>/', WalletBalanceView.as_view()),
    path('<uuid:wallet_id>/operation', WalletOperationView.as_view()),
]
